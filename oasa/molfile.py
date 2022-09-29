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
import re
import sys
import time

from oasa import converter_base
from oasa import plugin
from oasa import molecule

class Molfile(plugin.Plugin):

    name = "molfile"
    read = 1
    write = 1

    def __init__(self, structure=None):
        "Initializes the Molfile class."""
        self.structure = structure

    def set_structure(self, structure):
        self.structure = structure

    def get_structure(self):
        return self.structure

    def read_file(self, input_file):
        self._read_header(input_file)
        self._read_body(input_file)

    def _read_header(self, input_file):
        for i in range(3):
            input_file.readline()

    def _read_body(self, input_file):
        atoms = read_molfile_value(input_file, 3, conversion=int)
        bonds = read_molfile_value(input_file, 3, conversion=int)
        # nothing more interesting
        input_file.readline()
        # read the structure
        self.structure = molecule.Molecule()
        for i in range(atoms):
            a = self._read_atom(input_file)
            self.structure.add_vertex(v=a)
        for k in range(bonds):
            b, i, j = self._read_bond(input_file)
            self.structure.add_edge(i, j, e=b)
        for line in input_file:
            if line.strip() == "M  END":
                break
            if line.strip().startswith("M  "):
                self._read_property(line.strip())
            # print(line.strip())

    def _read_atom(self, input_file):
        x = read_molfile_value(input_file, 10, conversion=float)
        y = read_molfile_value(input_file, 10, conversion=float)
        z = read_molfile_value(input_file, 10, conversion=float)
        read_molfile_value(input_file, 1)  # empty space
        symbol = read_molfile_value(input_file, 3)
        mass_diff = read_molfile_value(input_file, 2)
        charge, multi = self._read_molfile_charge(
            read_molfile_value(input_file, 3, conversion=int))
        input_file.readline()  # next line please
        ret = self.structure.create_vertex()
        ret.coords = (x, y, z)
        ret.charge = charge
        ret.symbol = symbol
        ret.multiplicity = multi
        return ret

    def _read_bond(self, input_file):
        # molfiles index from 1
        a1 = read_molfile_value(input_file, 3, conversion=int) - 1
        a2 = read_molfile_value(input_file, 3, conversion=int) - 1
        order = read_molfile_value(input_file, 3, conversion=int)
        bond_type = read_molfile_value(input_file, 3, conversion=int)
        type_remap = {0: 'n', 1: 'w', 6: 'h', 4: 'a'}
        bond_type = type_remap.get(bond_type, 'n')
        input_file.readline()  # next line please
        b = self.structure.create_edge()
        b.order = order
        b.type = bond_type
        return b, a1, a2

    def _read_property(self, prop):
        m = re.match("M\s+RAD\s+(\d+)(.*)", prop)
        if m:
            for at, rad in re.findall("(\d+)\s+(\d+)", m.group(2)):
                index = int(at)
                multi = int(rad)
                self.structure.vertices[index-1].multiplicity = multi
        m = re.match("M\s+CHG\s+(\d+)(.*)", prop)
        if m:
            for at, chg in re.findall("(\d+)\s+(-?\d+)", m.group(2)):
                index = int(at)
                charge = int(chg)
                self.structure.vertices[index-1].charge = charge

    def write_file(self, output_file):
        """file should be a writable file object"""
        if not self.structure:
            raise Exception("No structure to write")
        self._write_header(output_file)
        self._write_counts_line(output_file)
        self._write_body(output_file)
        self._write_m_lines(output_file)
        output_file.write('M  END\n')

    def get_text(self):
        return ''.join((
            self._get_header(), self._get_counts_line(), self._get_body(), 'M  END'
        ))

    def _write_header(self, input_file):
        input_file.write(self._get_header())

    def _get_header(self):
        return "\n\n\n"

    def _write_counts_line(self, input_file):
        input_file.write(self._get_counts_line())

    def _get_counts_line(self):
        atoms = len(self.structure.vertices)
        bonds = len(self.structure.edges)
        atom_lists = 0
        fff = 0  # obsolete
        chiral = 0
        stexts = 0
        obsolete = "  0  0  0  0"
        extras = 999
        mol_version = " V2000"
        return "%3d%3d%3d%3d%3d%3d%s%s%s\n" % (
            atoms, bonds, atom_lists, fff, chiral,
            stexts, obsolete, extras, mol_version
        )

    def _write_body(self, input_file):
        input_file.write(self._get_body())

    def _get_body(self):
        lines = []
        for a in self.structure.vertices:
            lines.append(self._get_atom_line(a))
        for b in self.structure.edges:
            lines.append(self._get_bond_line(b))
        return '\n'.join(lines)+'\n'

    def _get_atom_line(self, a):
        x = a.get_x()
        y = a.get_y()
        z = a.get_z()
        symbol = a.symbol
        mass_diff = 0
        charge = self._get_molfile_charge(a.charge, a.multiplicity)
        rest = "  0  0  0  0  0  0  0  0  0  0"
        return "%10.4f%10.4f%10.4f %-3s%2d%3d%s" % (x, y, z, symbol, mass_diff, charge, rest)

    def _get_bond_line(self, b):
        v1, v2 = b.get_vertices()
        a1 = self.structure.vertices.index(v1) + 1
        a2 = self.structure.vertices.index(v2) + 1
        order = b.order
        type_remap = {'n': 0, 'w': 1, 'h': 6, 'a': 4, 'b': 0, 'd': 0}
        bond_type = type_remap.get(b.type, 0)
        rest = "  0  0  0"
        return "%3d%3d%3d%3d%s" % (a1, a2, order, bond_type, rest)

    def _write_m_lines(self, input_file):
        m_lines = self._get_m_lines()
        if m_lines:
            input_file.write("\n".join(m_lines) + "\n")

    def _get_m_lines(self):
        # radicals
        radicals = {}
        i = 1
        for v in self.structure.vertices:
            if v.multiplicity != 1:
                radicals[i] = v.multiplicity
            i += 1
        if radicals:
            assert len(radicals) <= 8
            nums = sorted(radicals.keys())
            rads = " ".join(["%3d %3d" % (n, radicals[n]) for n in nums])
            rad_line = "M  RAD%3d %s" % (len(nums), rads)
        else:
            rad_line = None
        # return m_lines
        m_lines = [_f for _f in [rad_line] if _f]
        return m_lines

    def _read_molfile_charge(self, value):
        if value == 0:
            return (0, 1)
        ch = -(value-4)
        multi = ch == 0 and 2 or 1
        return (ch, multi)

    def _get_molfile_charge(self, charge, multiplicity):
        if charge == 0:
            if multiplicity == 1:
                return 0
            else:
                return 4
        else:
            return 4-charge


def read_molfile_value(input_file, length, strip=1, conversion=None):
    """reads specified number of characters, if strip strips whitespace,
    if conversion (a fuction taking one string argument) applies it;
    if empty string is obtained after stripping 0 is returned"""
    str = input_file.read(length)
    if strip:
        str = str.strip()
    if str == "":
        return 0
    if conversion:
        str = conversion(str)
    return str


reads_text = 1
reads_files = 1
writes_text = 1
writes_files = 1


def mol_to_text(molfile):
    molfile_object = Molfile()
    molfile_object.structure = molfile
    return molfile_object.get_text()


def mol_to_file(mol, output_file):
    molfile_object = Molfile()
    molfile_object.structure = mol
    molfile_object.write_file(output_file)


def file_to_mol(input_file):
    molfile_object = Molfile()
    molfile_object.read_file(input_file)
    return molfile_object.structure


def text_to_mol(text):
    return file_to_mol(StringIO(text))


class MolfileConverter(converter_base.ConverterBase):

    # standard converter attrs
    reads_text = True
    writes_text = True
    reads_files = True
    writes_files = True

    default_configuration = {
    }

    def __init__(self):
        pass

    def mols_to_text(self, structures):
        output_file = StringIO()
        self.mols_to_file(structures, output_file)
        return output_file.getvalue()

    def read_text(self, text):
        super().read_text(text)
        mf = StringIO(text)
        for molfile in self.read_file(mf):
            yield mol

    def read_file(self, input_file):
        super().read_file(input_file)
        chunk = []
        m = Molfile()
        for line in input_file:
            if line.strip() != "$$$$":
                chunk.append(line)
            else:
                m.read_file(StringIO("".join(chunk)))
                yield m.structure
                chunk = []
        if [line for line in chunk if line.strip()]:  # non empty lines
            m.read_file(StringIO("".join(chunk)))
            yield m.structure

    def mols_to_file(self, structures, output_file):
        super().mols_to_file(structures, output_file)
        molfile_object = Molfile()
        first = output_file.tell() == 0
        for mol in structures:
            if not first:
                output_file.write("$$$$\n")
            first = False
            molfile_object.structure = mol
            molfile_object.write_file(f)
        self.last_status = self.STATUS_OK


if __name__ == "__main__":

    if len(sys.argv) < 1:
        print("you must supply a filename")
        sys.exit()

    file_name = sys.argv[1]
    with open(file_name, 'r') as f:
        mol = file_to_mol(f)

    for a in mol.atoms:
        print(a.x, a.y)

    t = time.time()
    lens = sorted(map(len, mol.get_smallest_independent_cycles()))
    print(lens)
    print(time.time() - t)
    print("total %d rings" % len(lens))
    print(mol)
