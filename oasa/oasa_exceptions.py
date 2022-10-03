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


class OasaError(Exception):

    def __init__(self, *args, **kw):
        Exception.__init__(self, *args, **kw)


class OasaPeriodicTableError(OasaError):
    """exception for reporting periodic_table related error"""

    def __init__(self, id, value, symbol=None):
        OasaError.__init__(self)
        self.id = id
        self.value = value

    def __str__(self):
        return "OASA periodic_table error, id=%s, value=%s" % (self.id, self.value)


class OasaInvalidAtomSymbol(OasaError):
    """exception for reporting invalid atom symbol use"""

    def __init__(self, value, symbol):
        OasaError.__init__(self)
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return "Symbol '%s' not allowed (%s)" % (self.symbol, self.value)


class OasaInvalidValue(OasaError):
    """exception for reporting invalid values"""

    def __init__(self, meaning, value):
        OasaError.__init__(self)
        self.value = value
        self.meaning = meaning

    def __str__(self):
        return "The value for '%s' is not allowed (%s)" % (self.meaning, self.value)


class OasaNotImplementedError(OasaError):

    def __init__(self, where, what):
        OasaError.__init__(self)
        self.where = where
        self.what = what

    def __str__(self):
        return "'Not implemented' error in %s: %s" % (self.where, self.what)


class OasaInchiError(OasaError):

    def __init__(self, what):
        OasaError.__init__(self)
        self.what = what

    def __str__(self):
        return "InChI error: %s" % self.what


class OasaUnsupportedInchiVersionError(OasaError):

    def __init__(self, version):
        OasaError.__init__(self)
        self.version = version

    def __str__(self):
        return "The InChI has an unsupported version: %s" % self.version


class OasaSmilesError(OasaError):

    def __init__(self, value):
        OasaError.__init__(self)
        self.value = value

    def __str__(self):
        return "SMILES Error: %s" % self.value


class OasaStereochemistryError(OasaError):

    def __init__(self, value):
        OasaError.__init__(self)
        self.value = value

    def __str__(self):
        return "Stereochemistry Error: %s" % self.value
