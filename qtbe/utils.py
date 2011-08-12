
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

import re
import cgi

from libbe.util.utility import handy_time

def comment_html(comment):
    commenter = '<h4>' + unicode(comment.author) + ' said:</h4>'
    time = '<h5>on ' + handy_time(comment.time) + '</h5>'
    return commenter + plaintext2html(comment.body) + time

def plaintext2html(text, tabstop=4):
    """
    Convert plain text to HTML
    http://djangosnippets.org/snippets/19/
    """
    re_string = re.compile(r"""(?P<htmlchars>[<&>])|
                               (?P<space>^[ \t]+)|
                               (?P<lineend>\r\n|\r|\n)|
                               (?P<protocal>(^|\s)
                                    ((http|ftp)://.*?))(\s|$)""", re.S|re.M|re.I|re.X)
    def do_sub(m):
        c = m.groupdict()
        if c['htmlchars']:
            return cgi.escape(c['htmlchars'])
        if c['lineend']:
            return '<br>'
        elif c['space']:
            t = m.group().replace('\t', '&nbsp;'*tabstop)
            t = t.replace(' ', '&nbsp;')
            return t
        elif c['space'] == '\t':
            return ' '*tabstop;
        else:
            url = m.group('protocal')
            if url.startswith(' '):
                prefix = ' '
                url = url[1:]
            else:
                prefix = ''
            last = m.groups()[-1]
            if last in ['\n', '\r', '\r\n']:
                last = '<br>'
            return '%s<a href="%s">%s</a>%s' % (prefix, url, url, last)
    return re_string.sub(do_sub, text)

