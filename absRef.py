import pymatgen.io.vasp as vasp
import csv
import numpy as np
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
import pymatgen as mg
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.linewidth"] = 1.5

vr1 = vasp.Vasprun('ilmenite.xml')

energies1 = vr1.dielectric[0]

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = [list(row) for row in reader]

wv = []
sr = []

for a in data:
        wv.append(float(a[0]))
        sr.append(float(a[2]))

e = []

for k in wv:
        e.append(1239.84198433/k)

e11 = np.array(vr1.dielectric[1])
e11x = e11[:,0]
e11y = e11[:,1]
e11z = e11[:,2]
e12 = np.array(vr1.dielectric[2])
e12x = e12[:,0]
e12y = e12[:,1]
e12z = e12[:,2]

nx1 = np.sqrt(((np.sqrt(e11y**2 + e12y**2)) + e11y)/2)

kx1 = np.sqrt(((np.sqrt(e11y**2 + e12y**2)) - e11y)/2)

rx1 = ((nx1-1)**2 + kx1**2)/((nx1+1)**2 + kx1**2)

w1 = np.array(energies1)
ax1 = (1.012857816E5*kx1*w1)
vr2 = vasp.Vasprun('perovskite.xml')

energies2 = vr2.dielectric[0]

e21 = np.array(vr2.dielectric[1])
e21x = e21[:,0]
e21y = e21[:,1]
e21z = e21[:,2]
e22 = np.array(vr2.dielectric[2])
e22x = e22[:,0]
e22y = e22[:,1]
e22z = e22[:,2]

nx2 = np.sqrt(((np.sqrt(e21y**2 + e22y**2)) + e21y)/2)

kx2 = np.sqrt(((np.sqrt(e21y**2 + e22y**2)) - e21y)/2)

rx2 = ((nx2-1)**2 + kx2**2)/((nx2+1)**2 + kx2**2)

w2 = np.array(energies2)
ax2 = (1.012857816E5*kx2*w2)

vr3 = vasp.Vasprun('linbo3.xml')

energies3 = vr3.dielectric[0]

e31 = np.array(vr3.dielectric[1])
e31x = e31[:,0]
e31y = e31[:,1]
e31z = e31[:,2]
e32 = np.array(vr3.dielectric[2])
e32x = e32[:,0]
e32y = e32[:,1]
e32z = e32[:,2]

nx3 = np.sqrt(((np.sqrt(e31y**2 + e32y**2)) + e31y)/2)

kx3 = np.sqrt(((np.sqrt(e31y**2 + e32y**2)) - e31y)/2)

rx3 = ((nx3-1)**2 + kx3**2)/((nx3+1)**2 + kx3**2)

w3 = np.array(energies3)
ax3 = (1.012857816E5*kx3*w3)

plt.figure()
fig, ax = plt.subplots(figsize = (7,9), nrows=2,ncols=1,sharex=True,sharey=False)
fig.text(0.55, 0.63, 'Spectral Irradiance', fontsize = 12, fontweight='bold', ha='center')
fig.text(0.5, 0.915,'$\mathregular{MgSnO_3}$', fontsize = 24, fontweight='bold', ha='center')
fig.text(0.02, 0.69, 'Absorption Coefficient, α ($\mathregular{10^4 cm^{-1}}$)', fontsize = 14, fontweight='bold', va='center', rotation='vertical')
fig.text(0.968, 0.685, 'Spectral Irradiance (W $\mathregular{m^{-2} nm^{-1}}$)', fontsize = 14, fontweight='bold', va='center', rotation=270)
fig.text(0.5, 0.05, 'Energy (eV)', fontsize = 14, fontweight='bold', ha='center')
fig.text(0.02, 0.3, 'Reflectivity', fontsize = 14, fontweight='bold', va='center', rotation='vertical')

axis1 = plt.subplot(211)
plt.plot(energies1, ax1/10000, 'b', label = 'Ilmenite')
plt.plot(energies2, ax2/10000, 'r-.', label = 'Perovskite')
plt.plot(energies3, ax3/10000, 'g--', label = '$\mathregular{LiNbO_3 type}$')
plt.grid('on')
plt.legend(loc='upper left', bbox_to_anchor=(-0.02, 1.02), fontsize=12, frameon = False, columnspacing=1.25,handlelength=1.75)
plt.minorticks_on()
plt.xlim(1,3.5)
plt.ylim(0,1.09)

axis2 = axis1.twinx()
axis2.plot(e,sr,color='#0f0f0f',lw = 0.75)
axis2.set_xlim(1,3.5)
axis2.set_ylim(0,1.95)
axis2.minorticks_on()
axis2.fill_between(e, sr, facecolor="yellow", alpha = 0.3, label = 'AM 1.5 G Spectral Irradiance')
axis2.legend(loc='upper right',fontsize=12, bbox_to_anchor=(0.95, 0.9465),frameon = False, handlelength=1.75)

plt.subplot(212)
plt.plot(energies1, rx1, 'b', label = 'Ilmenite')
plt.plot(energies2, rx2, 'r-.', label = 'Perovskite')
plt.plot(energies3, rx3, 'g--', label = '$\mathregular{LiNbO_3 type}$')
plt.grid('on')
plt.legend(loc='upper left',fontsize=12, frameon = False, columnspacing=1.25,handlelength=1.75)
plt.minorticks_on()
plt.xlim(1,3.5)
plt.ylim(0.04,0.099)
plt.subplots_adjust(hspace=0)

plt.savefig('AbsRef.pdf')
plt.close()
