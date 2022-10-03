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


from io import StringIO
import sys
import time
import xml.dom.minidom as dom

from oasa import smiles
from oasa import dom_extensions as dom_ext
from oasa import plugin
from oasa import atom
from oasa import bond
from oasa import molecule
from oasa import known_groups
from oasa import periodic_table as PT
from oasa import coords_generator


def read_cdml(text):
    """returns the last molecule for now"""
    doc = dom.parseString(text)
    path = "//molecule"
    do_not_continue_this_mol = 0
    for mol_el in dom_ext.simpleXPathSearch(doc, path):
        atom_id_remap = {}
        mol = molecule.Molecule()
        groups = []
        for atom_el in dom_ext.simpleXPathSearch(mol_el, "atom"):
            name = atom_el.getAttribute('name')
            if not name:
                #print("this molecule has an invalid symbol")
                do_not_continue_this_mol = 1
                break
            pos = dom_ext.simpleXPathSearch(atom_el, 'point')[0]
            x = cm_to_float_coord(pos.getAttribute('x'))
            y = cm_to_float_coord(pos.getAttribute('y'))
            z = cm_to_float_coord(pos.getAttribute('z'))
            if name in PT.periodic_table:
                # its really an atom
                a = atom(symbol=name,
                         charge=atom_el.getAttribute('charge') and int(
                             atom_el.getAttribute('charge')) or 0,
                         coords=(x, y, z))
                mol.add_vertex(v=a)
            elif name in cdml_to_smiles:
                # its a known group
                group = smiles.text_to_mol(cdml_to_smiles[name], calc_coords=0)
                a = group.vertices[0]
                a.x = x
                a.y = y
                a.z = z
                mol.insert_a_graph(group)
            atom_id_remap[atom_el.getAttribute('id')] = a
        if do_not_continue_this_mol:
            break

        for bond_el in dom_ext.simpleXPathSearch(mol_el, "bond"):
            type = bond_el.getAttribute('type')
            if type[1] == '0':
                # we ignore bonds with order 0
                continue
            v1 = atom_id_remap[bond_el.getAttribute('start')]
            v2 = atom_id_remap[bond_el.getAttribute('end')]
            e = bond(order=int(type[1]), type=type[0])
            mol.add_edge(v1, v2, e=e)

        if mol.is_connected():
            # this is here to handle diborane and similar weird things
            yield mol
        else:
            for comp in mol.get_disconnected_subgraphs():
                yield comp


def cm_to_float_coord(x):
    if not x:
        return 0
    if x[-2:] == 'cm':
        return float(x[:-2])*72/2.54
    else:
        return float(x)

reads_text = 1
reads_files = 1
writes_text = 0
writes_files = 0


def file_to_mol(f):
    return text_to_mol(f.read())


def text_to_mol(text):
    gen = read_cdml(text)
    try:
        mol = next(gen)
    except StopIteration:
        return None
    calculate_coords(mol, bond_length=-1)
    return mol

if __name__ == '__main__':

    if len(sys.argv) < 1:
        print("you must supply a filename")
        sys.exit()

    file_name = sys.argv[1]
    with open(file_name, 'r') as f:
        mol = file_to_mol(f)

    t = time.time()
    lens = sorted(map(len, mol.get_all_cycles()))
    print(lens)
    print(time.time() - t)
    print("total %d rings" % len(lens))

    print(mol)
