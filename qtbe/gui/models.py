
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


from PySide.QtCore import Qt, QAbstractTableModel


class BugTableModel(QAbstractTableModel):
    """Bug model for table view"""
    _bugs = []

    def _get_bugs(self):
        """Getter for bugs property"""
        return self._bugs

    def _set_bugs(self, bugs):
        """Setter for bugs property"""
        self._bugs = bugs
        self.reset()

    bugs = property(_get_bugs, _set_bugs, doc="list of loaded bugs")

    @property
    def header(self):
        """Titles of the column header"""
        return ('Title', 'Status', 'Severity', 'Assigned',)

    def load_data(self, bugs):
        """Convenient method to load data and reset view"""
        self.bugs = bugs
        self.reset()

    def rowCount(self, parent):
        """Number of rows, i.e., bugs loaded"""
        return len(self.bugs)

    def columnCount(self, parent):
        """Number of properties to show in the view"""
        return len(self.header)

    def headerData(self, section, orientation, role):
        """Header titles"""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]
            else:
                return self.bugs[section].id.user()

    def data(self, index, role):
        """Actual data to show in a cell"""
        if role == Qt.DisplayRole:
            return {
                0: lambda x: x.summary,
                1: lambda x: x.status,
                2: lambda x: x.severity,
                3: lambda x: x.assigned,
            }[index.column()](self.bugs[index.row()])

