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


import re

from warnings import warn

from oasa import atom
from oasa import chem_vertex
from oasa import oasa_exceptions
from oasa import periodic_table as PT


class QueryAtom(chem_vertex.ChemVertex):

    attrs_to_copy = chem_vertex.ChemVertex.attrs_to_copy + ("symbols",)

    def __init__(self, coords=None):
        """Initiliazes the QueryAtom class."""
        super().__init__(self, coords=coords)
        self.symbols = set()
        self.free_sites = 0
        self._symbol = None
        self._free_sites = None

    def matches(self, other):
        if not isinstance(other, atom.Atom):
            return False
        # halogens
        for sym in self.symbols:
            if sym == other.symbol:
                return True
            elif sym == "X":
                if other.symbol in ("F", "Cl", "Br", "I"):
                    return True
            # Q (any except H,C)
            elif sym == "Q":
                if other.symbol not in "HC":
                    return True
            # A (any except H)
            elif sym == "A":
                if other.symbol != "H":
                    return True
            # R - anything
            elif sym == "R":
                return True

        return False

    @property
    def symbol(self):
        """Atom symbol."""
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if symbol in list(PT.periodic_table.keys()):
            if not "query" in PT.periodic_table[symbol]:
                warn(
                    "Setting normal atom symbol to a query_atom instance, do you mean it?"
                )
            self.symbols = set([symbol])
        else:
            self.symbols = parse_query_definition(symbol)

        self._symbol = symbol

    @property
    def free_sites(self):
        """Atom's free sites."""
        return self._free_sites

    @free_sites.setter
    def free_sites(self, free_sites):
        self._free_sites = free_sites

    def __str__(self):
        return "query atom '%s'" % str(self.symbol)

def is_query_definition(text):
    matcher = re.compile("\[([A-Z][a-z]?,)*[A-Z][a-z]?\]")
    return matcher.match(text) and True or False

def parse_query_definition(text):
    if is_query_definition(text):
        syms = set(map(str, text[1:-1].split(",")))
        for sym in syms:
            if sym not in list(PT.periodic_table.keys()):
                raise oasa_exceptions.OasaInvalidAtomSymbol(
                    "invalid symbol in query definition", sym
                )
        return syms
    else:
        raise oasa_exceptions.OasaInvalidAtomSymbol(
            "not valid query definition", text
        )
