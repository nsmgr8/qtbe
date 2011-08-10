#!/usr/bin/env python

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

from distutils.core import setup

setup(
    name='Qt Bugs Everywhere',
    version='0.1a',
    description='Graphical user interface for bugtracker "Bugs Everywhere" supporting distributed revision control',
    url='http://bugseverywhere.org/',
    packages=['qtbe', 'qtbe.gui'],
    scripts=['qtbeapp'],
)

