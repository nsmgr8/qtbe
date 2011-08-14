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

from qtbe import VERSION

setup(
    name='QtBE',
    version=VERSION,
    url='https://github.com/nsmgr8/qtbe',
    download_url='https://github.com/nsmgr8/qtbe/zipball/{0}'.format(VERSION),
    author='M Nasimul Haque',
    author_email='nasim.haque@gmail.com',
    description='Graphical user interface for bugtracker "Bugs Everywhere" supporting distributed revision control',
    packages=['qtbe', 'qtbe.gui'],
    scripts=['qtbeapp'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: X11 Applications :: Qt',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Operating System :: OS Independent',
                 'Topic :: Software Development :: Bug Tracking',
    ],
)

