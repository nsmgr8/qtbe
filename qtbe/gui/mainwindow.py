
# Copyright (C) 2011 Nasimul Haque <nasim.haque@gmail.com>
#
# This file is part of Qt Bugs Everywhere.
#
# Qt Bugs Everywhere is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 2 of the License, or (at your
# option) any later version.
#
# Qt Bugs Everywhere is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Qt Bugs Everywhere.  If not, see <http://www.gnu.org/licenses/>.

import os

from PySide.QtGui import (QMainWindow, QFileDialog, QMessageBox, QHeaderView,
                          QAbstractItemView, QSortFilterProxyModel)

from ui_mainwindow import Ui_MainWindow
from models import BugTableModel
from qtbe.utils import comment_html

from libbe import storage, bug, bugdir
from libbe.command.depend import get_blocks, add_block, remove_block, get_blocked_by
from libbe.util.utility import handy_time
from libbe.ui.util.user import get_user_id


EMPTY = storage.util.settings_object.EMPTY

class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window of the app."""

    def __init__(self, parent=None):
        """Initialize the window, setup connections, populate initial data."""
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.statusCombo.addItems(bug.status_values)
        self.severityCombo.addItems(bug.severity_values)
        self.statusCombo.insertSeparator(len(bug.active_status_def))
        status_def = bug.active_status_def + bug.inactive_status_def
        tooltip = '\n'.join([': '.join(s) for s in status_def])
        self.statusCombo.setToolTip(tooltip)
        tooltip = '\n'.join([': '.join(s) for s in bug.severity_def])
        self.severityCombo.setToolTip(tooltip)

        self.action_New.triggered.connect(self.newProject)
        self.action_Open.triggered.connect(self.openProject)
        self.action_Close.triggered.connect(self.closeProject)
        self.bugFilterCombo.currentIndexChanged.connect(self.filter_bugs)
        self.propertyCombo.currentIndexChanged.connect(self.filter_property)
        self.saveBugButton.clicked.connect(self.create_bug)
        self.saveCommentButton.clicked.connect(self.add_comment)
        self.saveDetailsButton.clicked.connect(self.save_detail)
        self.discardDetailsButton.clicked.connect(self.display_bug)
        self.removeBugButton.clicked.connect(self.remove_bug)
        self.updateAllButton.clicked.connect(self.bulk_update)
        self.addFilterButton.clicked.connect(self.add_filter)
        self.cancelFilterButton.clicked.connect(self.clear_filter)
        self.filterBugsButton.clicked.connect(self.filter_bugs)

        self.project = None
        self.model = BugTableModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.bugTable.setModel(self.proxy_model)
        self.bugTable.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
        self.bugTable.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
        self.bugTable.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
        self.bugTable.horizontalHeader().setMinimumSectionSize(60)
        self.bugTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bugTable.selectionModel().selectionChanged.connect(self.select_bug)

        self.customFilterBox.setVisible(False)

    def _get_project(self):
        """Getter for project property"""
        return self._project

    def _set_project(self, path):
        """Setter for project property"""
        self._project = path
        if not path:
            self.projectTitle.setText('')
            self.newCommentBox.setVisible(False)
            self.newBugBox.setVisible(False)
            self._enable_controls(False)
        else:
            self.projectTitle.setText(path.split(os.path.sep)[-1])
            self._enable_controls()
        self.enable_bug_view(False)
        self.clear_filter()
    project = property(_get_project, _set_project, doc="the absolute path of the project")

    def _enable_controls(self, enable=True):
        """Enable/disable UI for opened/closed project"""
        self.mainBox.setEnabled(enable)
        self.label.setVisible(not enable)

    def newProject(self):
        """Open a new project"""
        self.openProject(is_new=True)

    def openProject(self, is_new=False):
        """Open an existing project"""
        title = is_new and 'Create new project' or 'Open project'
        path = QFileDialog.getExistingDirectory(self, title)
        if path and self.project != path:
            self._open_store(path, is_new)

    def closeProject(self):
        """Close a project"""
        self.project = None
        self.model.bugs = []
        self.enable_bug_view(False)
        self.newBugButton.setChecked(False)
        self.assignedCombo.clear()
        self.targetCombo.clear()
        self.bugFilterCombo.setCurrentIndex(0)

    def _open_store(self, path, is_new=False):
        """Open the store of the project, initialize the bugdir and load bugs"""
        store = storage.get_storage(path)
        try:
            if is_new:
                store.init()
            else:
                store.connect()
            if self.project:
                self.closeProject()
            self.user = get_user_id(store)
            version = store.version()
            self.vcsLabel.setText('None' if version == '0' else version)
            try:
                self.bd = bugdir.BugDir(store, from_storage=True)
            except:
                self.bd = bugdir.BugDir(store, from_storage=False)
            self.project = path
            self.reload_bugs()
            self.load_assignees()
            self.load_targets()
        except storage.ConnectionError as e:
            print e
            message = 'No project found. Would you like to initialize a new project?'
        except OSError as e:
            print e
            message = 'Project already exists. Would you like to open instead?'
        else:
            message = None
        if message:
            if self.confirm_action(message):
                self._open_store(path, not is_new)

    def reload_bugs(self, active=True):
        """Load all the bugs filtering on active status"""
        # FIXME: lazy loading of bugs should be considered
        self.bd.load_all_bugs()
        if active:
            filter_list = bug.status_values[:len(bug.active_status_def)]
        else:
            filter_list = bug.status_values[len(bug.active_status_def):]
        bugs = [b for b in self.bd if b.status in filter_list]
        self.model.bugs = bugs
        self.current_bug = None
        self.bugsLabel.setText(str(len(bugs)))

    def load_assignees(self):
        """Find and save all assignees for this project including the current user"""
        self.assignees = list(set([unicode(bug.assigned) for bug in self.bd if
            bug.assigned and bug.assigned != EMPTY]))
        if len(self.assignees) > 0:
            if self.user not in self.assignees:
                self.assignees.append(self.user)
            self.assignees.sort(key=unicode.lower)
        else:
            self.assignees = [self.user]
        self.assignedCombo.clear()
        self.assignedCombo.addItems([''] + self.assignees)

    def load_targets(self):
        """Load targets"""
        self.targets = [b for b in self.bd if b.severity == "target"]
        targets = [unicode(b.summary) for b in self.targets]
        targets.sort(key=unicode.lower)
        self.targetCombo.clear()
        self.targetCombo.addItems([''] + targets)

    def select_bug(self, new, old):
        """Slot for the bugTable selection changes. ``old`` is unused for now
        but required by Qt4 slot signature requirement.
        """
        n_select = len(self.bugTable.selectedIndexes())
        n_column = len(self.model.header)
        try:
            index = self.proxy_model.mapToSource(new.indexes()[0])
            bug = self.model.bugs[index.row()]
            if n_select > n_column:
                self.enable_bug_view(False)
                self.current_bug = None
                self.updateAllButton.setEnabled(True)
            else:
                self.display_bug(bug)
                self.updateAllButton.setEnabled(False)
            self.removeBugButton.setEnabled(True)
        except IndexError:
            self.enable_bug_view(False)
            self.removeBugButton.setEnabled(False)

    def select_current_bug(self, bug=None):
        """A convenience method to select a bug in the table"""
        if bug:
            self.current_bug = bug
        row = self.model.bugs.index(self.current_bug)
        index = self.model.index(row, 0)
        index = self.proxy_model.mapFromSource(index)
        self.bugTable.selectRow(index.row())

    def enable_bug_view(self, enable=True):
        """Enable/disable bug view"""
        self.addCommentButton.setEnabled(enable)
        self.saveDetailsButton.setEnabled(enable)
        self.discardDetailsButton.setEnabled(enable)
        self.bugTitle.setText('')
        self.shortLabel.setText('')
        self.idLabel.setText('')
        self.creatorLabel.setText('')
        self.createdLabel.setText('')
        self.reporterLabel.setText('')
        self.bugCommentBrowser.setHtml('')
        self.assignedCombo.setCurrentIndex(0)
        self.targetCombo.setCurrentIndex(0)
        self.addCommentButton.setChecked(False)
        self.updateAllButton.setEnabled(False)
        if not enable:
            self.current_bug = None

    def display_bug(self, bug=None):
        """Display currently selected bug or the bug passed via argument"""
        if bug:
            self.current_bug = bug
        else:
            bug = self.current_bug
        self.enable_bug_view()
        self.bugTitle.setText(bug.summary)
        self.shortLabel.setText(bug.id.user())
        self.idLabel.setText(bug.uuid)
        self.creatorLabel.setText(bug.creator)
        self.createdLabel.setText(handy_time(bug.time))
        self.reporterLabel.setText(bug.reporter)

        self.load_combos()
        self.load_comments()

    def load_comments(self):
        """Load all the comments for current bug"""
        comments = '<hr />'.join([comment_html(c) for c in self.current_bug.comments()])
        if not comments:
            comments = '<i>No comment yet!</i>'
        self.bugCommentBrowser.setHtml(comments)

    def load_combos(self):
        """Update the combo boxes for bug properties"""
        if not self.current_bug:
            return
        target = ''
        bug = self.current_bug
        blocks = get_blocks(self.bd, bug)
        for b in blocks:
            blocker = self.bd.bug_from_uuid(b.uuid)
            if blocker.severity == 'target':
                target = blocker.summary
        combos = [
            (self.statusCombo, bug.status),
            (self.severityCombo, bug.severity),
            (self.assignedCombo, bug.assigned),
            (self.targetCombo, target),
        ]
        self.assignedCombo.setCurrentIndex(0)
        self.targetCombo.setCurrentIndex(0)
        for combo, field in combos:
            for i in range(combo.count()):
                if combo.itemText(i) == field:
                    combo.setCurrentIndex(i)

    def create_bug(self):
        """Create a new bug"""
        summary = self.newBugEdit.text().strip()
        if summary:
            bug = self.bd.new_bug(summary=summary)
            bug.creator = self.user
            bug.reporter = self.user
            bug.save()
            self.reload_bugs()
            self.select_current_bug(bug)
            self.newBugEdit.setText('')
            self.statusbar.showMessage('A new bug {0} has been '
                    'added'.format(self.current_bug.id.user()))

    def add_comment(self):
        """Add a comment to the current bug. Comments are now flat, not threaded."""
        body = self.newCommentEdit.toPlainText().strip()
        if body:
            comment = self.current_bug.comment_root.new_reply(body=body)
            comment.author = self.user
            self.current_bug.save()
            self.display_bug()
            self.newCommentEdit.setPlainText('')
            self.statusbar.showMessage('New comment added to '
                    '{0}'.format(self.current_bug.id.user()))

    def save_detail(self):
        """Save updated properties to the current bug"""
        status = self.statusCombo.currentText()
        severity = self.severityCombo.currentText()
        assigned = self.assignedCombo.currentText()
        target = self.targetCombo.currentText()

        is_changed = self.current_bug.status != status or \
            self.current_bug.severity != severity or \
            self.current_bug.assigned != assigned

        if is_changed:
            self.current_bug.severity = severity
            self.current_bug.status = status
            self.current_bug.assigned = assigned
            self.current_bug.save()
            self.model.reset()
            self.load_targets()

        def remove_all_targets():
            """remove all targets for a bug, b"""
            for b in blocks:
                if b.severity == 'target':
                    remove_block(b, self.current_bug)

        blocks = get_blocks(self.bd, self.current_bug)
        if not target:
            is_changed = True
            remove_all_targets()
        else:
            for t in self.targets:
                if t.summary == target:
                    if t not in blocks:
                        is_changed = True
                        remove_all_targets()
                        add_block(t, self.current_bug)
                    break

        if is_changed:
            self.load_combos()
            self.select_current_bug()
            self.statusbar.showMessage('Changes to details for the bug {0} '
                    'has been saved'.format(self.current_bug.id.user()))

    def bulk_update(self):
        """Bulk update properties of selected bugs"""
        if not self.confirm_action('Are you sure to update all selected bugs?'):
            return
        indexes = set([self.proxy_model.mapToSource(index).row() for index in self.bugTable.selectedIndexes()])
        bugs = [self.model.bugs[index] for index in indexes]

        status = self.statusCombo.currentText()
        severity = self.severityCombo.currentText()
        assigned = self.assignedCombo.currentText()
        target = self.targetCombo.currentText()

        def remove_all_targets():
            for b in blocks:
                if b.severity == 'target':
                    remove_block(b, bug)

        for bug in bugs:
            bug.severity = severity
            bug.status = status
            bug.assigned = assigned
            bug.save()
            blocks = get_blocks(self.bd, bug)
            if not target:
                remove_all_targets()
            else:
                for t in self.targets:
                    if t.summary == target:
                        if t not in blocks:
                            remove_all_targets()
                            add_block(t, bug)
                        break

        self.model.reset()
        self.load_targets()
        self.load_combos()
        self.statusbar.showMessage('Updated all selected bugs')

    def remove_bug(self):
        """Remove selected bugs from the project"""
        indexes = set([self.proxy_model.mapToSource(index).row() for index in self.bugTable.selectedIndexes()])
        bugs = [self.model.bugs[index] for index in indexes]
        if len(bugs) > 0 and not self.confirm_action('Are you sure to remove selected bugs?'):
            return
        ids = []
        for bug in bugs:
            ids.append(bug.id.user())
            self.bd.remove_bug(bug)
        self.reload_bugs()
        self.enable_bug_view(False)
        self.removeBugButton.setEnabled(False)
        self.statusbar.showMessage('Removed %s bug(s)' % ', '.join(ids))

    def filter_bugs(self, value=None):
        """Filter bugs on active status"""
        if not value:
            bugs = self.bd
            if self.filter_set:
                status = self.filter_set.get('status')
                severity = self.filter_set.get('severity')
                target = self.filter_set.get('target')
                assigned = self.filter_set.get('assigned')
                if target:
                    for t in self.targets:
                        if t.summary == target:
                            target = t
                            break
                    bugs = get_blocked_by(self.bd, target)
                if assigned:
                    bugs = [b for b in bugs if b.assigned == assigned]
                if severity:
                    bugs = [b for b in bugs if b.severity == severity]
                if status:
                    bugs = [b for b in bugs if b.status == status]
            self.model.bugs = bugs
            self.current_bug = None
            self.bugsLabel.setText(str(len(bugs)))
            self.enable_bug_view(False)
        elif value == 'custom':
            self.customFilterBox.setVisible(True)
            self.propertyCombo.setCurrentIndex(0)
            self.valueCombo.clear()
            self.valueCombo.addItems(bug.status_values)
        else:
            self.clear_filter()
            self.customFilterBox.setVisible(False)
            self.reload_bugs(value == 'active')
            self.enable_bug_view(False)

    def filter_property(self, value):
        items = {
            'status': bug.status_values,
            'severity': bug.severity_values,
            'target': [t.summary for t in self.targets],
            'assigned': self.assignees,
        }[value]
        self.valueCombo.clear()
        self.valueCombo.addItems(items)

    def add_filter(self):
        try:
            key, value = self.propertyCombo.currentText(), self.valueCombo.currentText()
            self.filter_set[key] = value
        except:
            self.filter_set = {key: value}
        text = ''
        for key in self.filter_set:
            text += '<b>{0}</b>: {1}<br/>'.format(key, self.filter_set[key])
        self.customFilterLabel.setText(text)

    def clear_filter(self):
        self.customFilterLabel.setText('Select filters')
        self.filter_set = None

    def confirm_action(self, message):
        """Convenient method for user confirmation on action"""
        result = QMessageBox.warning(self, self.windowTitle(), message, QMessageBox.Ok | QMessageBox.Cancel)
        return result == QMessageBox.Ok

