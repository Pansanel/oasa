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

import sys
import copy

from warnings import warn

from oasa.graph import vertex
import oasa.periodic_table as PT


class ChemVertex(vertex.Vertex):
    """Parent class of atoms, groups etc.

    It defines common properties for vertices used in chemical context.
    It should not be instantiated directly, but rather inherited from.
    """
    attrs_to_copy = vertex.Vertex.attrs_to_copy + \
        ("charge", "x", "y", "z", "multiplicity", "valency", "charge", "free_sites")

    def __init__(self, coords=None):
        super().__init__()
        self.charge = 0
        self.free_sites = 0
        # None means not set (used)
        if coords:
            self.x, self.y, self.z = coords
        else:
            self.x = None
            self.y = None
            self.z = None
        self._multiplicity = 1

    def matches(self, other):
        if other is self:
            return False
        return True

    @property
    def coords(self):
        """Atom coordinates."""
        return self.x, self.y, self.z

    @coords.setter
    def coords(self, coords):
        if len(coords) == 2:
            self.x, self.y = coords
            self.z = 0
        elif len(coords) == 3:
            self.x, self.y, self.z = coords
        else:
            raise Exception("wrong number of coordinates")

    @property
    def charge(self):
        """Atom charge."""
        return self._charge

    @charge.setter
    def charge(self, charge):
        self._clean_cache()
        self._charge = charge

    @property
    def multiplicity(self):
        """Return the atom multiplicity."""
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        self._clean_cache()
        self._multiplicity = multiplicity

    @property
    def valency(self):
        """Returns the atom valency."""
        return self._valency

    @valency.setter
    def valency(self, valency):
        self._clean_cache()
        self._valency = valency

    @property
    def occupied_valency(self):
        """Atom's occupied valency."""
        i = 0
        for b in list(self._neighbors.keys()):
            ord = b.order
            if ord == 4:
                ord = 1
            i += ord
        return i

    @property
    def free_valency(self):
        """Atom's free valency."""
        try:
            return self._cache['free_valency']
        except KeyError:
            x = self.valency - self.occupied_valency
            self._cache['free_valency'] = x
            return x

    @property
    def weight(self):
        """Atom weight."""
        try:
            return PT.periodic_table[self.symbol]['weight']
        except:
            return 0

    @property
    def free_sites(self):
        """Atom's free sites."""
        really_free = self._free_sites - self.occupied_valency
        if really_free < 0:
            return 0
        else:
            return really_free

    @free_sites.setter
    def free_sites(self, free_sites):
        self._free_sites = free_sites

    def get_x(self):
        return self.x or 0

    def get_y(self):
        return self.y or 0

    def get_z(self):
        return self.z or 0

    def has_aromatic_bonds(self):
        for b in list(self._neighbors.keys()):
            if b.aromatic:
                return 1
        return 0

    def bond_order_changed(self):
        """called by a bond when its order was changed"""
        self._clean_cache()

    def get_hydrogen_count(self):
        return 0
