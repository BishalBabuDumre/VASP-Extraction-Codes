import pymatgen as mg
import pymatgen.io.vasp as vasp

structure = mg.Structure.from_file('POSCAR')
hskp = mg.symmetry.bandstructure.HighSymmKpath(structure)
kpoints = mg.io.vasp.Kpoints.automatic_linemode(10, hskp)

kpoints.write_file('KPOINTS')
