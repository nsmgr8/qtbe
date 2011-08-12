
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

from PySide.QtGui import QMainWindow, QFileDialog, QMessageBox, QHeaderView, QAbstractItemView

from ui_mainwindow import Ui_MainWindow
from models import BugTableModel
from qtbe.utils import comment_html

from libbe import storage, bug, bugdir
from libbe.command.depend import get_blocks, add_block, remove_block
from libbe.util.utility import handy_time
from libbe.ui.util.user import get_user_id


EMPTY = storage.util.settings_object.EMPTY

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.statusCombo.addItems(bug.status_values)
        self.severityCombo.addItems(bug.severity_values)
        status_def = bug.active_status_def + bug.inactive_status_def
        tooltip = '\n'.join([': '.join(s) for s in status_def])
        self.statusCombo.setToolTip(tooltip)
        tooltip = '\n'.join([': '.join(s) for s in bug.severity_def])
        self.severityCombo.setToolTip(tooltip)

        self.action_New.triggered.connect(self.newProject)
        self.action_Open.triggered.connect(self.openProject)
        self.action_Close.triggered.connect(self.closeProject)
        self.saveBugButton.clicked.connect(self.create_bug)
        self.saveCommentButton.clicked.connect(self.add_comment)
        self.saveDetailsButton.clicked.connect(self.save_detail)
        self.discardDetailsButton.clicked.connect(self.display_bug)

        self.project = None
        self.model = BugTableModel()
        self.bugTable.setModel(self.model)
        self.bugTable.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
        self.bugTable.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
        self.bugTable.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
        self.bugTable.horizontalHeader().setMinimumSectionSize(60)
        self.bugTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bugTable.selectionModel().selectionChanged.connect(self.select_bug)

    def _get_project(self):
        return self._project

    def _set_project(self, path):
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
    project = property(_get_project, _set_project)

    def _enable_controls(self, enable=True):
        self.mainBox.setEnabled(enable)
        self.label.setVisible(not enable)

    def newProject(self):
        self.openProject(is_new=True)

    def openProject(self, is_new=False):
        title = is_new and 'Create new project' or 'Open project'
        path = QFileDialog.getExistingDirectory(self, title)
        if path and self.project != path:
            self._open_store(path, is_new)

    def closeProject(self):
        self.project = None
        self.model.bugs = []
        self.enable_bug_view(False)
        self.newBugButton.setChecked(False)
        self.assignedCombo.clear()
        self.targetCombo.clear()

    def _open_store(self, path, is_new=False):
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
        except storage.ConnectionError as e:
            print e
            message = 'No project found. Would you like to initialize a new project?'
        except OSError as e:
            print e
            message = 'Project already exists. Would you like to open instead?'
        else:
            message = None
        if message:
            answer = QMessageBox.question(self, self.windowTitle(), message,
                                          QMessageBox.Ok | QMessageBox.Cancel)
            if answer == QMessageBox.Ok:
                self._open_store(path, not is_new)

    def reload_bugs(self):
        self.bd.load_all_bugs()
        bugs = list(self.bd)
        bugs.sort(key=lambda x: x.severity)
        self.model.bugs = bugs

        self.load_assignees()
        self.load_targets()

    def load_assignees(self):
        assignees = list(set([unicode(bug.assigned) for bug in self.model.bugs if
            bug.assigned and bug.assigned != EMPTY]))
        if len(assignees) > 0:
            if self.user not in assignees:
                assignees.append(self.user)
            assignees.sort(key=unicode.lower)
        else:
            assignees = [self.user]
        self.assignedCombo.clear()
        self.assignedCombo.addItems([''] + assignees)

    def load_targets(self):
        self.targets = [b for b in self.model.bugs if b.severity == "target"]
        targets = [unicode(b.summary) for b in self.targets]
        targets.sort(key=unicode.lower)
        self.targetCombo.clear()
        self.targetCombo.addItems([''] + targets)

    def select_bug(self, new, old):
        try:
            bug = self.model.bugs[new.indexes()[0].row()]
            self.display_bug(bug)
        except IndexError:
            self.enable_bug_view(False)

    def enable_bug_view(self, enable=True):
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

    def display_bug(self, bug=None):
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
        comments = '<hr />'.join([comment_html(c) for c in self.current_bug.comments()])
        if not comments:
            comments = '<i>No comment yet!</i>'
        self.bugCommentBrowser.setHtml(comments)

    def load_combos(self):
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
        summary = self.newBugEdit.text().strip()
        if summary:
            bug = self.bd.new_bug(summary=summary)
            bug.creator = self.user
            bug.reporter = self.user
            self.reload_bugs()
            self.display_bug(bug)
            self.newBugEdit.setText('')
            self.statusbar.showMessage('A new bug {0} has been '
                    'added'.format(self.current_bug.id.user()))

    def add_comment(self):
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
        status = self.statusCombo.currentText()
        severity = self.severityCombo.currentText()
        assigned = self.assignedCombo.currentText()
        target = self.targetCombo.currentText()

        is_changed = False
        if self.current_bug.status != status:
            is_changed = True
            self.current_bug.status = status
        if self.current_bug.severity != severity:
            is_changed = True
            self.current_bug.severity = severity
        if self.current_bug.assigned != assigned:
            is_changed = True
            self.current_bug.assigned = assigned

        if is_changed:
            self.current_bug.save()
            self.model.reset()
            self.load_targets()

        def remove_all_targets():
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
            self.statusbar.showMessage('Changes to details for the bug {0} '
                    'has been saved'.format(self.current_bug.id.user()))

