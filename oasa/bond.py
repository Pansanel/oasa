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


"""The bond resides here.

"""

# the order 1,2,3 is self-evident, order=4 means aromatic bond for which no
# localized bond order is available


import sys
import math
from warnings import warn
from oasa.graph import edge


class Bond(edge.Edge):
    """Based on edge, however the vertices are not a Set anymore.

    We need to preserve the order (for instance for wedge bonds).
    Type is:
    'n' - normal
    'w' - wedge
    'h' - hatch
    'a' - adder
    'b' - bold
    'd' - dash
    """
    attrs_to_copy = edge.Edge.attrs_to_copy + ("order", "aromatic", "type")

    def __init__(self, vs=[], order=1, type='n'):
        """Initializes the Bond class."""
        super().__init__(vs=vs)
        self.set_vertices(vs)
        self.aromatic = None  # None means it was not set
        self._order = order
        self.type = type
        self.properties_ = {}
        self.stereochemistry = None

    def __str__(self):
        if self._vertices:
            return "bond between %s %s" % tuple(map(str, self._vertices))
        else:
            return "bond, no vertices set"

    def matches(self, other):
        if self.order == other.order:
            return True
        return False

    @property
    def vertices(self):
        """Tuple of 2 vertices (start, end)."""
        return self._vertices

    @vertices.setter
    def vertices(self, vs=[]):
        """Sets the vertices this edge connects."""
        assert len(vs) == 2 or len(vs) == 0
        # if len( vs) == 2 and vs[0] == vs[1]:
        #  warn( "creating bond with both ends equal", UserWarning, 2)
        self._vertices = list(vs)

    @property
    def order(self):
        """Bond order.

        1-3 for normal bonds,
        4   for aromatic bonds for which localized order is not available,
        for localized aromatic bonds check the bond.aromatic boolean attribute.
        """
        if self._order is None and self.aromatic:
            return 4
        else:
            return self._order

    @order.setter
    def order(self, order):
        [a.bond_order_changed() for a in self._vertices]
        if order == 4:
            self._order = None
            self.aromatic = 1
        else:
            self._order = order

    @property
    def length(self):
        """Returns the bond length."""
        if len(self._vertices) == 2:
            v1, v2 = self._vertices
            return math.sqrt((v1.x-v2.x)**2 + (v1.y-v2.y)**2)
        else:
            return 0
