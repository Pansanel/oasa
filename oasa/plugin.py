# Copyright (C) 2003-2008 Beda Kosata <beda@zirael.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>


class plugin(object):
    """Basic plugin interface.

    """
    name = "plugin"
    read = 0
    write = 0

    def __init__(self):
        pass

    def set_structure(self, structure):
        pass

    def get_structure(self, structure):
        pass

    def read_file(self, file):
        pass

    def write_file(self, file):
        pass
