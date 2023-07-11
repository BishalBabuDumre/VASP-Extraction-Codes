import pymatgen.io.vasp as mg

vr = mg.Vasprun('vasprun.xml')
bs = vr.get_band_structure()
gap = bs.get_band_gap()
