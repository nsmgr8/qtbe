
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

"""A graphical user interface for the bug manager "Bugs Everywhere". This is a
single window bug manager built on top of PySide, a Qt4 wrapper for python"""


VERSION = '0.1'

def main():
    """Main entry to run the app"""
    import sys
    from PySide.QtGui import QApplication
    from gui.mainwindow import MainWindow

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    return app.exec_()

