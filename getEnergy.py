import pymatgen.io.vasp as mg

vr = mg.Vasprun('vasprun.xml')

energy = vr.final_energy

print(energy)
