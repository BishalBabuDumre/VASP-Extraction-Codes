import pymatgen as mg

s = mg.Structure.from_file('POSCAR')

prim = s.get_primitive_structure()

prim.to(fmt='poscar',filename='primitivePOSCAR')
