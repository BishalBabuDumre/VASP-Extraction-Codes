import yaml
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
import scipy.interpolate as ip
import numpy as np
from matplotlib.ticker import MultipleLocator
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.linewidth"] = 1.5



full_data5 = []
file5 = open('ilmenitePhononPDOS.dat','r')
for f5 in file5:
        row5= f5.split()
        full_data5.append(row5)

e1 = []
mg1 = []
sn1 = []
o1 = []
total1 = []

for f in full_data5:
        e1.append(float(f[0]))
        mg1.append(float(f[1])+float(f[2])+float(f[3])+float(f[4])+float(f[5])+float(f[6]))
        sn1.append(float(f[7])+float(f[8])+float(f[9])+float(f[10])+float(f[11])+float(f[12]))
        o1.append(float(f[13])+float(f[14])+float(f[15])+float(f[16])+float(f[17])+float(f[18])+float(f[19])+float(f[20])+float(f[21])+float(f[22])+float(f[23])+float(f[24])+float(f[25])+float(f[26])+float(f[27])+float(f[28])+float(f[29])+float(f[30]))
        total1.append(float(f[1])+float(f[2])+float(f[3])+float(f[4])+float(f[5])+float(f[6])+float(f[7])+float(f[8])+float(f[9])+float(f[10])+float(f[11])+float(f[12])+float(f[13])+float(f[14])+float(f[15])+float(f[16])+float(f[17])+float(f[18])+float(f[19])+float(f[20])+float(f[21])+float(f[22])+float(f[23])+float(f[24])+float(f[25])+float(f[26])+float(f[27])+float(f[28])+float(f[29])+float(f[30]))

full_data6 = []
file6 = open('perovskitePhononDOS.dat','r')
for f6 in file6:
        row6= f6.split()
        full_data6.append(row6)

e2 = []
mg2 = []
sn2 = []
o2 = []
total2 = []

for f in full_data6:
        e2.append(float(f[0]))
        mg2.append(float(f[1]))
        sn2.append(float(f[2]))
        o2.append(float(f[3])+float(f[4])+float(f[5]))
        total2.append(float(f[1])+float(f[2])+float(f[3])+float(f[4])+float(f[5]))

full_data7 = []
file7 = open('liNbO3TypePhononPDOS.dat','r')
for f7 in file7:
        row7 = f7.split()
        full_data7.append(row7)

e3 = []
mg3 = []
sn3 = []
o3 = []
total3 = []

for f in full_data7:
        e3.append(float(f[0]))
        mg3.append(float(f[1])+float(f[2])+float(f[3])+float(f[4])+float(f[5])+float(f[6]))
        sn3.append(float(f[7])+float(f[8])+float(f[9])+float(f[10])+float(f[11])+float(f[12]))
        o3.append(float(f[13])+float(f[14])+float(f[15])+float(f[16])+float(f[17])+float(f[18])+float(f[19])+float(f[20])+float(f[21])+float(f[22])+float(f[23])+float(f[24])+float(f[25])+float(f[26])+float(f[27])+float(f[28])+float(f[29])+float(f[30]))
        total3.append(float(f[1])+float(f[2])+float(f[3])+float(f[4])+float(f[5])+float(f[6])+float(f[7])+float(f[8])+float(f[9])+float(f[10])+float(f[11])+float(f[12])+float(f[13])+float(f[14])+float(f[15])+float(f[16])+float(f[17])+float(f[18])+float(f[19])+float(f[20])+float(f[21])+float(f[22])+float(f[23])+float(f[24])+float(f[25])+float(f[26])+float(f[27])+float(f[28])+float(f[29])+float(f[30]))

file = open('1color.csv','r')
for f in file:
        c0 = f.split()
d0=[]
for aa in range (60):
        d0.append(c0[aa])
for aa in range (60):
        d0.append(c0[aa])

with open('ilmeniteBand.yaml') as file:
        documents = yaml.full_load(file)

for item1, doc1 in documents.items():
        if item1=='phonon':
                dict1={item1:doc1}

a = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

doc2 = dict1.get('phonon')

for i in doc2:
        x = i.get('distance')
        t = 0
        for j in i.get('band'):
                a[t].append([x,j.get('frequency')])
                t = t + 1

with open('perovskiteBand.yaml') as file:
        documents = yaml.full_load(file)

for item1, doc1 in documents.items():
        if item1=='phonon':
                dict1={item1:doc1}

b = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

doc2 = dict1.get('phonon')

for i in doc2:
        x = i.get('distance')
        t = 0
        for j in i.get('band'):
                b[t].append([x,j.get('frequency')])
                t = t + 1

with open('liNbO3TypeBand.yaml') as file:
        documents = yaml.full_load(file)

for item1, doc1 in documents.items():
        if item1=='phonon':
                dict1={item1:doc1}

p = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

doc2 = dict1.get('phonon')
#ss = []
for i in doc2:
        x = i.get('distance')
#       y = i.get('q-position')
#       ss.append(x)
        t = 0
        for j in i.get('band'):
                p[t].append([x,j.get('frequency')])
                t = t + 1
#print(ss)
z = np.linspace(0.0, 1.2018322, num=100000)

fig = plt.figure(figsize=(7,10.5))
fig.text(0.52, 0.92,'$\mathregular{MgSnO_3}$', fontsize = 21, fontweight='bold',  ha='center')
fig.text(0.52, 0.888,'Ilmenite', fontsize = 13, fontweight='bold',  ha='center')
fig.text(0.52, 0.608,'Perovskite', fontsize = 13, fontweight='bold',  ha='center')
fig.text(0.52, 0.325,'$\mathregular{LiNbO_3 type}$', fontsize = 13, fontweight='bold',  ha='center')
ax0 = plt.subplot2grid((3,3),(0,0),colspan=2, rowspan = 1)
for i1 in range(90):
        distance = []
        freq = []
        hai1 = 0
        for i2 in a[i1]:
                freq.append(a[i1][hai1][1])
                distance.append(a[i1][hai1][0])
                hai1 = hai1 + 1
        g = ip.interp1d(distance,freq,kind=1)
        plt.plot(z, g(z), color = d0[i1], ls = '-',lw = 1)

plt.xlim(0.0, 1.2018322)
plt.ylim(-6.29,25.99)
plt.axvline(x=0, color='k', ls = '-',lw=1)
plt.axvline(x=0.11001100, color='k', ls = '-',lw=1)
plt.axvline(x=0.22002200, color='k', ls = '-',lw=1)
plt.axvline(x=0.33003300, color='k', ls = '-',lw=1)
plt.axvline(x=0.52074380, color='k', ls = '-',lw=1)
plt.axvline(x=0.55645810, color='k', ls = '-',lw=1)
plt.axvline(x=0.66646910, color='k', ls = '-',lw=1)
plt.axvline(x=0.78213210, color='k', ls = '-',lw=1)
plt.axvline(x=0.89779510, color='k', ls = '-',lw=1)
plt.axvline(x=1.00780610, color='k', ls = '-',lw=1)
plt.axvline(x=1.2018322, color='k', ls = '-',lw=1)
ax0.set_xlabel('Wave Vector k')
ax0.set_ylabel('Frequency (THz)')
ax0.set_xticks([0, 0.11001100, 0.22002200, 0.33003300, 0.52074380, 0.55645810, 0.66646910, 0.78213210, 0.89779510, 1.00780610, 1.20183220])
ax0.set_xticklabels(['X','Γ','Y','L','Γ','Z','N','Γ','M','R','Γ'], fontsize = 9)
ax0.yaxis.set_minor_locator(MultipleLocator(1))
ax0.grid()
plt.minorticks_on()

z = np.linspace(0, 1.0659938, num=100000)
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2, rowspan = 1)
for i1 in range(15):
        distance = []
        freq = []
        hai1 = 0
        for i2 in b[i1]:
                freq.append(b[i1][hai1][1])
                distance.append(b[i1][hai1][0])
                hai1 = hai1 + 1
        g = ip.interp1d(distance,freq,kind=1)
        plt.plot(z, g(z), color = c0[i1], ls = '-',lw = 1)
plt.xlim(0,1.0659938)
plt.ylim(-10.49,27.99)
plt.axvline(x=0, color='k', ls = '-',lw=1)
plt.axvline(x=0.12452500, color='k', ls = '-',lw=1)
plt.axvline(x=0.24905010, color='k', ls = '-',lw=1)
plt.axvline(x=0.42515510, color='k', ls = '-',lw=1)
plt.axvline(x=0.64083880, color='k', ls = '-',lw=1)
plt.axvline(x=0.81694380, color='k', ls = '-',lw=1)
plt.axvline(x=0.94146880, color='k', ls = '-',lw=1)
plt.axvline(x=1.06599380, color='k', ls = '-',lw=1)
ax2.set_xlabel('Wave Vector k')
ax2.set_ylabel('Frequency (THz)')
ax2.set_xticks([0,0.12452500,0.24905010,0.42515510,0.64083880,0.81694380,0.94146880,1.06599380])
ax2.set_xticklabels(['Γ','X','M','Γ','R','X','M','R'], fontsize = 9)
ax2.yaxis.set_minor_locator(MultipleLocator(1))
ax2.grid()
plt.minorticks_on()

z = np.linspace(0, 1.0980705, num=100000)
ax3 = plt.subplot2grid((3,3),(2,0),colspan=2, rowspan = 1)
for i1 in range(90):
        distance = []
        freq = []
        hai1 = 0
        for i2 in p[i1]:
                freq.append(p[i1][hai1][1])
                distance.append(p[i1][hai1][0])
                hai1 = hai1 + 1
        g = ip.interp1d(distance,freq,kind=1)
        plt.plot(z, g(z), color = d0[i1], ls = '-',lw = 1)
plt.xlim(0,1.0980705)
plt.ylim(0,20.88)
plt.axvline(x=0, color='k', ls = '-',lw=1)
plt.axvline(x=0.10891120, color='k', ls = '-',lw=1)
plt.axvline(x=0.16310110, color='k', ls = '-',lw=1)
plt.axvline(x=0.26791860, color='k', ls = '-',lw=1)
plt.axvline(x=0.32821490, color='k', ls = '-',lw=1)
plt.axvline(x=0.52012750, color='k', ls = '-',lw=1)
plt.axvline(x=0.60446560, color='k', ls = '-',lw=1)
plt.axvline(x=0.72696120, color='k', ls = '-',lw=1)
plt.axvline(x=0.75564120, color='k', ls = '-',lw=1)
plt.axvline(x=0.80804990, color='k', ls = '-',lw=1)
plt.axvline(x=0.86108860, color='k', ls = '-',lw=1)
plt.axvline(x=0.97557490, color='k', ls = '-',lw=1)
plt.axvline(x=1.09807050, color='k', ls = '-',lw=1)
ax3.set_xlabel('Wave Vector k')
ax3.set_ylabel('Frequency (THz)')
ax3.set_xticks([0,0.10891120,0.16310110,0.26791860,0.32821490,0.52012750,0.60446560,0.72696120,0.75564120,0.80804990,0.86108860,0.97557490,1.09807050])
ax3.set_xticklabels(['Γ','L','B_1','B','Z','Γ','X','Q','F','P_1','Z','L','P'], fontsize = 9)
ax3.yaxis.set_minor_locator(MultipleLocator(1))
ax3.grid()
plt.minorticks_on()

ax1 = plt.subplot2grid((3,3),(0,2),colspan=1, rowspan = 1)
g8 = ip.interp1d(e1, total1, kind = 'cubic')
curve1 = ip.interp1d(e1, mg1, kind = 'cubic')
curve2 = ip.interp1d(e1, sn1, kind = 'cubic')
curve3 = ip.interp1d(e1, o1, kind = 'cubic')
x12 = np.linspace(-7.3904460862,28.0196661062, num=100000)
ax1.fill_between(g8(x12), x12, facecolor="grey", alpha = 0.3, label='Total \nDOS')
plt.plot(curve1(x12),x12, 'r-.',label='Mg')
plt.plot(curve2(x12),x12, 'g--',label='Sn')
plt.plot(curve3(x12),x12, 'b',label='O')
ax1.xaxis.set_minor_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(MultipleLocator(1))
ax1.yaxis.set_ticklabels([])
ax1.set_xticks([0,4,8])
ax1.set_xticklabels(['0','4','8'],fontsize = 9)
plt.xlim(0,8)
plt.legend(loc='center right', ncol=1, fontsize=8,bbox_to_anchor=(1.48,0.5),handlelength = 1.8, frameon = False)
plt.ylim(-7.49,28.49)
ax1.grid()
ax1.set_xlabel('Phonon DOS (states/THz)')
plt.minorticks_on()

ax4 = plt.subplot2grid((3,3),(1,2),colspan=1, rowspan = 1)
g8 = ip.interp1d(e2, total2, kind = 'cubic')
curve1 = ip.interp1d(e2, mg2, kind = 'cubic')
curve2 = ip.interp1d(e2, sn2, kind = 'cubic')
curve3 = ip.interp1d(e2, o2, kind = 'cubic')
x12 = np.linspace(-13.4052630846, 30.0244248463, num=100000)
ax4.fill_between(g8(x12), x12, facecolor="grey", alpha = 0.3, label='Total \nDOS')
plt.plot(curve1(x12),x12, 'r-.',label='Mg')
plt.plot(curve2(x12),x12, 'g--',label='Sn')
plt.plot(curve3(x12),x12, 'b',label='O')
ax4.xaxis.set_minor_locator(MultipleLocator(1))
ax4.yaxis.set_minor_locator(MultipleLocator(1))
ax4.yaxis.set_ticklabels([])
ax4.set_xticks([0,1,2])
ax4.set_xticklabels(['0','1','2'],fontsize = 9)
plt.xlim(0,2)
plt.legend(loc='center right', ncol=1, fontsize=8,bbox_to_anchor=(1.48,0.5),handlelength = 1.8, frameon = False)
plt.ylim(-6.29,25.99)
ax4.grid()
ax4.set_xlabel('Phonon DOS (states/THz)')
plt.minorticks_on()

ax5 = plt.subplot2grid((3,3),(2,2),colspan=1, rowspan = 1)
g8 = ip.interp1d(e3, total3, kind = 'cubic')
curve1 = ip.interp1d(e3, mg3, kind = 'cubic')
curve2 = ip.interp1d(e3, sn3, kind = 'cubic')
curve3 = ip.interp1d(e3, o3, kind = 'cubic')
x12 = np.linspace(-2.1041555342, 22.7655659602, num=100000)
ax5.fill_between(g8(x12), x12, facecolor="grey", alpha = 0.3, label='Total \nDOS')
plt.plot(curve1(x12),x12, 'r-.',label='Mg')
plt.plot(curve2(x12),x12, 'g--',label='Sn')
plt.plot(curve3(x12),x12, 'b',label='O')
ax5.xaxis.set_minor_locator(MultipleLocator(1))
ax5.yaxis.set_minor_locator(MultipleLocator(1))
ax5.yaxis.set_ticklabels([])
plt.xlim(0,8)
ax5.set_xticks([0,4,8])
ax5.set_xticklabels(['0','4','8'],fontsize = 9)
plt.legend(loc='center right', ncol=1, fontsize=8,bbox_to_anchor=(1.48,0.5),handlelength = 1.8, frameon = False)
plt.ylim(0,20.88)
ax5.grid()
ax5.set_xlabel('Phonon DOS (states/THz)')
plt.minorticks_on()

plt.subplots_adjust(wspace=0.075)
plt.subplots_adjust(hspace=0.37)
plt.savefig('bandsPhonon.png')
plt.close()
