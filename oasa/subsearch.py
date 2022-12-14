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


import os
import sys
import time

from oasa import smiles
from oasa.graph import digraph
from oasa import subsearch_data

class SubstructureSearchManager(object):

    substructure_def_file = os.path.join(
        os.path.dirname(__file__), "subsearch_data.txt")
    ring_def_file = os.path.join(
        os.path.dirname(__file__), "subsearch_rings.txt")

    def __init__(self):
        # graph describing the relations between individual structures
        self.structures = digraph.Digraph()
        self.search_trees = []  # list of substructure instances that for a tree
        self.rings = {}
        self.fill_data()

    def fill_data(self):
        for struct in subsearch_data.structures:
            compound_type, name, smiles_string, to_ignore = struct
            sub_structure = Substructure(
                name, compound_type,
                smiles_str=smiles_string,
                atoms_to_ignore=to_ignore
            )
            v = self.structures.create_vertex()
            v.value = sub_structure
            self.structures.add_vertex(v)
        for ring_desc in subsearch_data.rings:
            name, smiles_string, ring_hash = ring_desc
            rng = Ring(name, smiles_string, ring_hash=ring_hash)
            self.rings[ring_hash] = rng
        # the following takes some time
        self._analyze_structure_dependencies()

    def _read_structure_file(self, name=""):
        """may be used to read data directly from source txt files.
        is deprecated in favor of automatically build subsearch_data.py module"""
        with open(name or self.substructure_def_file, 'r') as input_file:
            for line in input_file:
                l = line.strip()
                if l and not l.startswith("#"):
                    parts = l.split(";")
                    if len(parts) < 3:
                        raise ValueError("Wrong line in data file: '%s'" % l)
                    compound_type, name, smiles_string = [
                        x.strip() for x in parts[:3]]
                    if len(parts) > 3:
                        to_ignore = parts[3].strip()
                    else:
                        to_ignore = ""
                    to_ignore = list(
                        map(int, [_f for _f in to_ignore.split(",") if _f]))
                    if not name.strip():
                        name = compound_type
                    sub_structure = Substructure(
                        name,
                        compound_type,
                        smiles_str=smiles_string,
                        atoms_to_ignore=to_ignore
                    )
                    vertex = self.structures.create_vertex()
                    vertex.value = sub_structure
                    self.structures.add_vertex(vertex)
        self._analyze_structure_dependencies()

    def _read_ring_file(self, name=""):
        """may be used to read data directly from source txt files.
        is deprecated in favor of automatically build subsearch_data.py module"""
        with open(name or self.ring_def_file, 'r') as input_file:
            for line in input_file:
                l = line.strip()
                if l and not l.startswith("#"):
                    parts = [x.strip() for x in l.split(";")]
                    if len(parts) != 3:
                        raise ValueError("Wrong line in data file: '%s'" % l)
                    name, smiles_string, ring_hash = parts
                    rng = Ring(name, smiles_string, ring_hash=ring_hash)
                    self.rings[ring_hash] = rng

    def _analyze_structure_dependencies(self):
        for v1 in self.structures.vertices:
            for v2 in self.structures.vertices:
                if v1 is not v2:
                    sub1 = v1.value
                    sub2 = v2.value
                    if sub1.structure.contains_substructure(sub2.structure):
                        self.structures.add_edge(v2, v1)

    def _find_head_structures(self):
        for v1 in self.structures.vertices:
            v1.properties_['in_links'] = []
            for v2 in self.structures.vertices:
                if v1 in v2.neighbors:
                    v1.properties_['in_links'].append(v2.value)
        heads = []
        for v in self.structures.vertices:
            if not v.properties_['in_links']:
                # we have got a top of the tree
                heads.append(v)
        return heads

    def _compute_search_trees(self):
        heads = self._find_head_structures()
        assert heads
        for head in heads:
            # distance = self.structures.mark_vertices_with_distance_from(head)
            dv = [(v.properties_['d'], v)
                  for v in self.structures.vertices if 'd' in v.properties_]
            dv.sort(reverse=True)
            for vert_dist, vertice in dv:
                for par_dist, parent in dv:
                    if parent.value in vertice.properties_['in_links']:
                        if vertice.value not in parent.value.children:
                            # this ensures only one copy of a substructure in a tree
                            parent.value.children.append(vertice.value)
                        break
        return [h.value for h in heads]

    def get_more_specific_substructure(self, s1, s2):
        """returns 1 if s1 is more specific,
                   2 if s2 is more specific,
                   3 if both are the same,
                   4 if the relationship cannot be established
                   (there is not connection between s1 and s2 in the
                   substructure interdependency graph - this signifies
                   a problem, probably in the matching algorithm
                   """
        if s1 is s2:
            return 3
        # just find vertices corresponding to s1 and s2
        v1 = None
        v2 = None
        for v in self.structures.vertices:
            if v.value == s1:
                v1 = v
            elif v.value == s2:
                v2 = v
        assert v1
        assert v2
        p1 = self.structures.path_exists(v1, v2)
        p2 = self.structures.path_exists(v2, v1)
        if (p1 and p2) or (not p1 and not p2):
            # both paths exist or none does - this should not happen
            return 4
        if p1:
            return 2
        if p2:
            return 1

    def find_substructures_in_mol(self, mol_data):
        # get the hits
        hits2 = []
        for v in self.structures.vertices:
            struct = v.value
            ms = struct.find_matches(mol_data)
            hits2 += ms
        # weed out the hits that match inside a ring
        ring_hits = self.find_rings_in_mol(mol_data)
        hits = []
        for hit in hits2:
            keep = True
            for rhit in ring_hits:
                if set(rhit.get_significant_atoms()) & set(hit.get_significant_atoms()):
                    keep = False
                    break
            if keep:
                hits.append(hit)
        # weed out overlapping hits - leave only the most significant ones
        hit_num = len(hits)
        to_delete = True
        while to_delete:
            to_delete = []
            for i, hit1 in enumerate(hits):
                for hit2 in hits[i+1:]:
                    if hit1 is not hit2:
                        if set(hit1.get_significant_atoms()) & set(hit2.get_significant_atoms()):
                            winner = self.get_more_specific_substructure(
                                hit1.substructure, hit2.substructure)
                            if winner == 1:
                                to_delete.append(hit2)
                            elif winner == 2:
                                to_delete.append(hit1)
                            elif winner == 3:
                                pass  # we preserve both hits
                            else:
                                raise ValueError(
                                    "Relationship between competing fragments could not be established,\nthere is probaly an error in the substructure matching code.")
                if to_delete:
                    break
            hits = [hit for hit in hits if not hit in to_delete]
        return ring_hits + hits

    def find_rings_in_mol(self, mol_data, detect_aromatic=True):
        hits = []
        if detect_aromatic:
            # this is necessary to correctly process fused aromatic rings
            # with improperly localized bonds
            mol_data.mark_aromatic_bonds()
        for ering in mol_data.get_smallest_independent_cycles_e():
            vring = mol_data.edge_subgraph_to_vertex_subgraph(ering)
            ring_mol = mol_data.get_new_induced_subgraph(vring, ering)
            # here we need to take care of aromatic bonds
            # this is needed to properly match naphthalene, etc.
            if detect_aromatic:
                for edge in ring_mol.edges:
                    if edge.aromatic:
                        edge.order = 4
                ring_mol.localize_aromatic_bonds()
            ring_hash = ring_mol.get_structure_hash()
            if ring_hash in self.rings:
                hit = RingMatch(vring, self.rings[ring_hash])
            else:
                ring_obj = Ring(None, smiles.mol_to_text(
                    ring_mol), ring_hash=ring_hash)
                self.rings[ring_hash] = ring_obj
                hit = RingMatch(vring, ring_obj)
            hits.append(hit)
        return hits


def data_files_to_python_module(structure_file=None, ring_file=None):
    with open("subsearch_data.py", 'w') as out:
        print("""# Copyright (C) 2003-2008 Beda Kosata <beda@zirael.org>
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

""", file=out)
        print("# Automatically generated file - may be overwritten at any time", file=out)
        print("structures = [", file=out)

        with open(structure_file or SubstructureSearchManager.substructure_def_file, 'r') as input_file:
            for line in input_file:
                l = line.strip()
                if l and not l.startswith("#"):
                    parts = [x.strip() for x in l.split(";")]
                    if len(parts) < 3:
                        print("Invalid line in src file:", line[:-1], file=sys.stderr)
                    elif len(parts) == 3:
                        parts.append("")
                    to_ignore = list(
                        map(int, [_f for _f in parts[3].split(",") if _f]))
                    parts[3] = to_ignore
                    if not parts[1]:
                        parts[1] = parts[0]
                    print(tuple(parts), ",", file=out)
            print("]", file=out)

        with open(ring_file or SubstructureSearchManager.ring_def_file, 'r') as input_file:
            print("rings = [", file=out)
            for line in input_file:
                l = line.strip()
                if l and not l.startswith("#"):
                    parts = [x.strip() for x in l.split(";")]
                    print(tuple(parts), ",", file=out)
            print("]", file=out)


class Substructure(object):

    def __init__(self, name, compound_type, smiles_str="", atoms_to_ignore=None):
        """Initializes the Substructure class."""
        self.name = name
        self.compound_type = compound_type
        self.structure = None
        if smiles_str:
            self.read_smiles(smiles_str, atoms_to_ignore=atoms_to_ignore)
        self.children = []

    def __str__(self):
        return "<Substructure: %s: %s>" % (self.name, self.smiles_string)

    def read_smiles(self, smiles_string, atoms_to_ignore=None):
        self.smiles_string = smiles_string.strip()
        self.structure = smiles.text_to_mol(smiles_string, calc_coords=False)
        if atoms_to_ignore:
            self.atoms_to_ignore = [self.structure.vertices[x-1]
                                    for x in atoms_to_ignore]
        else:
            self.atoms_to_ignore = []

    def find_matches(self, mol_data):
        ret = []
        ms = list(mol_data.select_matching_substructures(
            self.structure, implicit_freesites=True, auto_cleanup=False))
        for atoms in ms:
            num = min(atoms[0].properties_['subsearch'].keys())
            atoms_in_fragment = [a.properties_[
                'subsearch'][num] for a in atoms]
            ret.append(SubstructureMatch(atoms, atoms_in_fragment, self))
        mol_data.clean_after_search(self.structure)
        return ret


class Ring(object):

    def __init__(self, name, smiles_str, ring_hash=None):
        """Initializes the Ring class."""
        self.name = name
        self.compound_type = "ring"
        self.smiles_string = smiles_str.strip()
        if ring_hash:
            self.ring_hash = ring_hash
        else:
            self.ring_hash = None  # read smiles and generate hash here?

    def __str__(self):
        return "<Ring: %s: %s>" % (self.name, self.smiles_string)


class SubstructureMatch(object):

    def __init__(self, atoms_found, atoms_searched, substruct):
        """Initializes the SubstructureMatch class.

        atoms_found are atoms in the molecule we searched in,
        atoms_searched are atoms in the fragment we used for search,
        (atoms_searched and atoms_found are guaranteed to have the same
        order, thus allowing matching between the two structures),
        substruct is the substructure instance"""
        self.substructure = substruct
        self.atoms_found = atoms_found
        self.atoms_searched = atoms_searched

    def __str__(self):
        return "<Match of %s with %d atoms (%d significant)>" % (self.substructure, len(self.atoms_found), len(self.get_significant_atoms()))

    def get_significant_atoms(self):
        ret = []
        for i, af in enumerate(self.atoms_found):
            atms = self.atoms_searched[i]
            if atms not in self.substructure.atoms_to_ignore:
                ret.append(af)
        return ret


class RingMatch(object):

    def __init__(self, atoms_found, ring_obj):
        """Initializes the RingMatch class."""
        self.substructure = ring_obj
        self.atoms_found = atoms_found

    def __str__(self):
        return "<RingMatch of %s>" % (self.substructure)

    def get_significant_atoms(self):
        return self.atoms_found


if __name__ == "__main__":
    # update the subsearch_data.py module
    data_files_to_python_module()
    t = time.time()
    ssm = SubstructureSearchManager()

    print("Read_structure_file: %.1fms" % (1000*(time.time() - t)))
    t = time.time()

    print(ssm.structures)
    dump = ssm.structures.get_graphviz_text_dump()
    with open("dump.dot", 'w') as f:
        f.write(dump)

    print("Graphviz dump: %.1fms" % (1000*(time.time() - t)))
    t = time.time()

    def print_tree(x, l):
        print(l*" ", x)  # , x.children
        for ch in x.children:
            print_tree(ch, l+2)

    text = 'C(=O)OCC'
    mol = smiles.text_to_mol(text, calc_coords=False)

    subs = ssm.find_substructures_in_mol(mol)
    for sub in subs:
        print(sub)

    print("Substructure search: %.1fms" % (1000*(time.time() - t)))
    t = time.time()
