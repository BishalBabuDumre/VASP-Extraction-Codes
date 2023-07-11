import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import scipy.interpolate as ip
import numpy as np
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.linewidth"] = 1.5
plt.rc('axes', axisbelow=True)

full_data1 = []
file1 = open('./ilmenite.lobster','r')
for f1 in file1:
        row1 = f1.split()
        full_data1.append(row1)
energy1 = []
a1 = []
b1 = []
c1 = []
d1 = []
for row1 in full_data1:
        energy1.append(float(row1[0]))
        a1.append(-1*float(row1[85]))
        b1.append(-1*float(row1[385]))
        c1.append(-1*float(row1[623]))
        d1.append(-1*float(row1[1]))
g1 = ip.interp1d(energy1, a1, kind = 'cubic')
h1 = ip.interp1d(energy1, b1, kind = 'cubic')
i1 = ip.interp1d(energy1, c1, kind = 'cubic')
j1 = ip.interp1d(energy1, d1, kind = 'cubic')

full_data2 = []
file2 = open('./perovskite.lobster','r')
for f2 in file2:
        row2 = f2.split()
        full_data2.append(row2)
energy2 = []
a2 = []
b2 = []
c2 = []
d2 = []
for row2 in full_data2:
        energy2.append(float(row2[0]))
        a2.append(-1*float(row2[19]))
        b2.append(-1*float(row2[43]))
        c2.append(-1*float(row2[55]))
        d2.append(-1*float(row2[1]))
g2 = ip.interp1d(energy2, a2, kind = 'cubic')
h2 = ip.interp1d(energy2, b2, kind = 'cubic')
i2 = ip.interp1d(energy2, c2, kind = 'cubic')
j2 = ip.interp1d(energy2, d2, kind = 'cubic')



full_data3 = []
file3 = open('./linbo3Type.lobster','r')
for f3 in file3:
        row3 = f3.split()
        full_data3.append(row3)
energy3 = []
a3 = []
b3 = []
c3 = []
d3 = []
for row3 in full_data3:
        energy3.append(float(row3[0]))
        a3.append(-1*float(row3[175]))
        b3.append(-1*float(row3[289]))
        c3.append(-1*float(row3[581]))
        d3.append(-1*float(row3[1]))
g3 = ip.interp1d(energy3, a3, kind = 'cubic')
h3 = ip.interp1d(energy3, b3, kind = 'cubic')
i3 = ip.interp1d(energy3, c3, kind = 'cubic')
j3 = ip.interp1d(energy2, d3, kind = 'cubic')


x = np.linspace(-10, 5, num=100000)

plt.figure()
fig,ax = plt.subplots(figsize = (7,9), nrows=3,ncols=1,sharex=True,sharey=False)
fig.text(0.025, 0.5,'-pCOHP',fontsize=16,fontweight='bold', rotation='vertical',va='center')
fig.text(0.5,0.05,'Energy, E - E$_{f}$ (eV)',fontsize=16,fontweight='bold', ha='center')
fig.text(0.52, 0.94,'$\mathregular{MgSnO_3}$', fontsize = 24, fontweight='bold',  ha='center')

ax1 = plt.subplot(311)
plt.plot(x, g1(x), 'b')
plt.plot(x, h1(x), 'r--')
plt.plot(x, i1(x), 'g-.')
plt.plot(x,j1(x), 'c', ls = 'dotted')
plt.text(2.08, 0.718,'Ilmenite', fontsize = 12, fontweight='bold')
plt.xlim(-8,5)
plt.minorticks_on()
plt.grid('on')
plt.axvline(x=0, color='k', ls = '--')
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

ax2 = plt.subplot(312)
plt.plot(x, g2(x), 'b')
plt.plot(x, h2(x), 'r--')
plt.plot(x, i2(x), 'g-.')
plt.plot(x, j2(x), 'c', ls = 'dotted')
plt.text(1.8, 0.278,'Perovskite', fontsize = 12, fontweight='bold')
plt.xlim(-8,5)
plt.minorticks_on()
plt.grid('on')
plt.axvline(x=0, color='k', ls = '--')
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

plt.subplot(313)
plt.plot(x, g3(x), 'b', label = 'Mg-O')
plt.plot(x, h3(x), 'r--', label = 'Sn-O')
plt.plot(x, i3(x), 'g-.', label = 'O-O')
plt.plot(x, j3(x), 'c', ls = 'dotted', label = 'Average')
plt.text(1.7, 0.72,'LiNbO$_{3}$ Type', fontsize = 12, fontweight='bold')
plt.xlim(-8,5)
plt.minorticks_on()
plt.grid('on')
plt.axvline(x=0, color='k', ls = '--')
plt.legend(loc='upper center',ncol=4,fontsize=14,bbox_to_anchor=(0.5,3.2235),columnspacing=1.25,handlelength=1.65)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
ax2.set_ylim(-0.35,0.6)
plt.subplots_adjust(hspace=0)
plt.savefig('COHP.pdf')
plt.close()
