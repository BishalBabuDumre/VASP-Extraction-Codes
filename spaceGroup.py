import pymatgen as mg
import pymatgen.symmetry.analyzer as sa

s = mg.Structure.from_file('POSCAR')
a = sa.SpacegroupAnalyzer(s,symprec=1,angle_tolerance=30)
n = a.get_space_group_number()
k = a.get_crystal_system()
r = a.get_space_group_symbol()

print(n,k,r)
