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


import copy


class Edge(object):

    attrs_to_copy = ("disconnected",)

    def __init__(self, vs=None):
        self.vertices = []
        if vs is None:
            vs = []
        self.set_vertices(vs)
        self.properties_ = {}
        self.disconnected = False

    def __str__(self):
        return "edge between %s %s" % tuple(map(str, self.vertices))

    def copy(self):
        other = self.__class__()
        for attr in self.attrs_to_copy:
            setattr(other, attr, copy.copy(getattr(self, attr)))
        return other

    def set_vertices(self, vs=None):
        # Ring perception algorithm relies on allowing both vertices
        # to be the same
        if vs is None:
            vs = []
        if vs and len(vs) == 2:
            self.vertices = list(vs)

    def get_vertices(self):
        return self.vertices

    @property
    def neighbor_edges(self):
        v1, v2 = self.vertices
        out1 = [e for e in v1.neighbor_edges if e != self]
        out2 = [e for e in v2.neighbor_edges if e != self]
        return out1 + out2

    def get_neighbor_edges2(self):
        """Return 2 lists of neighbor edges (one for one side, one for the other).

        """
        v1, v2 = self.vertices
        out1 = [e for e in v1.neighbor_edges if e != self]
        out2 = [e for e in v2.neighbor_edges if e != self]
        return out1, out2

    @property
    def disconnected(self):
        return self.disconnected

    @disconnected.setter
    def disconnected(self, d):
        self.disconnected = d
