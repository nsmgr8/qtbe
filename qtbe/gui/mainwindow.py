
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

from libbe import storage, bug, bugdir
from libbe.command.util import bug_comment_from_user_id
from libbe.util.utility import handy_time


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

        self.project = None
        self.model = BugTableModel()
        self.issueTable.setModel(self.model)
        self.issueTable.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
        self.issueTable.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
        self.issueTable.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
        self.issueTable.horizontalHeader().setMinimumSectionSize(60)
        self.issueTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.issueTable.selectionModel().selectionChanged.connect(self.select_bug)

    def _get_project(self):
        return self._project

    def _set_project(self, path):
        self._project = path
        if not path:
            self.projectTitle.setText('')
            self.newCommentBox.setVisible(False)
            self.newIssueBox.setVisible(False)
            self._enable_controls(False)
        else:
            self.projectTitle.setText(path.split(os.path.sep)[-1])
            self._enable_controls()
    project = property(_get_project, _set_project)

    def _enable_controls(self, value=True):
        self.mainBox.setEnabled(value)
        self.label.setVisible(not value)

    def newProject(self):
        self.openProject(is_new=True)

    def openProject(self, is_new=False):
        title = is_new and 'Create new project' or 'Open project'
        path = QFileDialog.getExistingDirectory(self, title)
        if path:
            self._open_store(path, is_new)

    def _open_store(self, path, is_new=False):
        store = storage.get_storage(path)
        try:
            if is_new:
                store.init()
            else:
                store.connect()
            if self.project:
                self.closeProject()
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
        self.model.bugs = list(self.bd)

        assignees = list(set([unicode(bug.assigned) for bug in self.model.bugs if
            bug.assigned != EMPTY]))
        assignees.sort(key=unicode.lower)
        self.assignedCombo.clear()
        self.assignedCombo.addItems([''] + assignees)

        targets = list(set([unicode(bug.summary) for bug in self.model.bugs if
            bug.severity == u"target"]))
        targets.sort(key=unicode.lower)
        self.milestoneCombo.clear()
        self.milestoneCombo.addItems([''] + targets)

    def closeProject(self):
        self.project = None
        self.enable_bug(False)
        self.assignedCombo.clear()
        self.milestoneCombo.clear()

    def select_bug(self, new, old):
        try:
            bug = self.model.bugs[new.indexes()[0].row()]
            self.display_bug(bug.id.long_user())
        except IndexError:
            self.enable_bug(False)

    def enable_bug(self, enable=True):
        self.addCommentButton.setEnabled(enable)
        self.issueTitle.setText('')
        self.shortLabel.setText('')
        self.idLabel.setText('')
        self.creatorLabel.setText('')
        self.createdLabel.setText('')
        self.reporterLabel.setText('')
        self.assignedCombo.setCurrentIndex(0)
        self.milestoneCombo.setCurrentIndex(0)
        self.addCommentButton.setChecked(False)

    def display_bug(self, bugid):
        self.enable_bug()
        bug, comment = bug_comment_from_user_id(self.bd, bugid)
        self.issueTitle.setText(bug.summary)
        self.shortLabel.setText(bug.id.user())
        self.idLabel.setText(bug.uuid)
        self.creatorLabel.setText(bug.creator)
        self.createdLabel.setText(handy_time(bug.time))
        self.reporterLabel.setText(bug.reporter)
        combos = [
            (self.statusCombo, bug.status),
            (self.severityCombo, bug.severity),
            (self.assignedCombo, bug.assigned),
        ]
        self.assignedCombo.setCurrentIndex(0)
        for combo, field in combos:
            for i in range(combo.count()):
                if combo.itemText(i) == field:
                    combo.setCurrentIndex(i)

