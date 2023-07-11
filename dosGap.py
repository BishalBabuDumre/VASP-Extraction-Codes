import pymatgen as mg

vr = mg.io.vasp.Vasprun('vasprun.xml')

dos = vr.complete_dos

print(dos.get_gap())
