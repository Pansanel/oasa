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


class Diedge(object):

    def __init__(self, vs=None):
        """Initializes the Diedge class."""
        self.vertices = []
        if vs is None:
            vs = []
        self.set_vertices(vs)
        self.properties_ = {}

    def __str__(self):
        return "Directed edge between %s %s" % tuple(map(str, self.vertices))

    def set_vertices(self, vs=None):
        if vs is None:
            vs = []
        if vs and len(vs) == 2:
            self.vertices = vs

    def get_vertices(self):
        return self.vertices

    @property
    def neighbor_edges(self):
        v1, v2 = self.vertices
        out1 = [e for e in v1.neighbor_edges if e != self]
        out2 = [e for e in v2.neighbor_edges if e != self]
        return out1 + out2

    def get_neighbor_edges2(self):
        """Return 2 lists of neighbor edges.

        The first list is for one site and the second for
        the other.
        """
        v1, v2 = self.vertices
        out1 = [e for e in v1.neighbor_edges if e != self]
        out2 = [e for e in v2.neighbor_edges if e != self]
        return out1, out2
