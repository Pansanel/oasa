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


from oasa import molecule


class Reaction(object):
    """Reaction representation."""

    def __init__(self, reactants=None, products=None, reagents=None):
        """Initializes the Reaciton class."""
        self.reactants = reactants or []
        self.products = products or []
        self.reagents = reagents or []

    def __str__(self):
        s = "\nreactants:\n"
        for i in self.reactants:
            s += "    {0}\n".format(i)
        s += "reagents:\n"
        for i in self.reagents:
            s += "    {0}\n".format(i)
        s += "products:\n"
        for i in self.products:
            s += "    {0}\n".format(i)

        return s


class ReactionComponent(object):
    """Represents one component of a reaction."""

    def __init__(self, mol=None, stoichiometry=1):
        """Initializes the ReacionComponent class."""
        self.stoichiometry = stoichiometry
        self.molecule = mol

    @property
    def molecule(self):
        return self.molecule

    @molecule.setter
    def molecule(self, mol):
        assert isinstance(mol, molecule.Molecule)
        self.molecule = mol

    @property
    def stoichiometry(self):
        return self.stoichiometry

    @stoichiometry.setter
    def stoichiometry(self, stoich):
        assert isinstance(stoich, (int, float))
        self.stoichiometry = stoich

    def __str__(self):
        return "%s * (%s)" % (self.stoichiometry, self.molecule)
