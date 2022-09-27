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


allNames = ['atom', 'bond', 'chem_vertex', 'coords_generator', 'config',
            'coords_optimizer', 'geometry', 'graph', 'inchi', 'known_groups',
            'linear_formula', 'molecule', 'molfile', 'name_database',
            'oasa_exceptions', 'periodic_table', 'query_atom', 'smiles',
            'stereochemistry', 'subsearch', 'svg_out', 'transform',
            'transform3d']

try:
    from oasa import cairo_out
except ImportError:
    CAIRO_AVAILABLE = False
else:
    allNames.append("cairo_out")
    CAIRO_AVAILABLE = True

# inchi_key
try:
    from oasa import inchi_key
except Exception as e:
    INCHI_KEY_AVAILABLE = False
else:
    allNames.append("inchi_key")
    INCHI_KEY_AVAILABLE = True

try:
    from oasa import name_database
except Exception as e:
    NAME_DATABASE_AVAILABLE = False
else:
    allNames.append("name_database")
    NAME_DATABASE_AVAILABLE = True

# structure_database requires sqlite
try:
    from oasa import structure_database
except Exception as e:
    STRUCTURE_DATABASE_AVAILABLE = False
else:
    allNames.append("structure_database")
    STRUCTURE_DATABASE_AVAILABLE = True

# pybel
try:
    from oasa import pybel_bridge
except Exception as e:
    PYBEL_AVAILABLE = False
else:
    allNames.append("pybel_bridge")
    PYBEL_AVAILABLE = True


__all__ = allNames
