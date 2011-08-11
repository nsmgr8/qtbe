
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

from PySide.QtGui import QMainWindow, QFileDialog

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.action_New.triggered.connect(self.newProject)
        self.action_Open.triggered.connect(self.openProject)
        self.action_Close.triggered.connect(self.closeProject)

        self.project = None

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
        self.openProject("Create a new project")

    def openProject(self, title=None):
        if not title:
            self.openProject("Open a project")
            return
        path = QFileDialog.getExistingDirectory(self, title)
        if path:
            self.project = path

    def closeProject(self):
        self.project = None

