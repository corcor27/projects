import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

print "Initialising..."

inj_v=0.75

#manually set injection value

def chi_p_1():
    data = []
    g = open('M40_INC_0.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_1 = [x[52] for x in data ]
    return Chi_p_1 

def chi_p_2():
    data = []
    g = open('M40_INC_10.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_2 = [x[52] for x in data ]
    return Chi_p_2     

def chi_p_3():
    data = []
    g = open('M40_INC_20.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_3 = [x[52] for x in data ]
    return Chi_p_3 

def chi_p_4():
    data = []
    g = open('M40_INC_30.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_4 = [x[52] for x in data ]
    return Chi_p_4 

def chi_p_5():
    data = []
    g = open('M40_INC_40.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_5 = [x[52] for x in data ]
    return Chi_p_5    

def chi_p_6():
    data = []
    g = open('M40_INC_50.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_6 = [x[52] for x in data ]
    return Chi_p_6 

def chi_p_7():
    data = []
    g = open('M40_INC_60.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_7 = [x[52] for x in data ]
    return Chi_p_7    

chi_p_INC_0 = chi_p_1()
INC_0_upper_90=np.percentile(chi_p_INC_0, 95)
INC_0_lower_90=np.percentile(chi_p_INC_0, 5)

chi_p_INC_10 = chi_p_2()
INC_10_upper_90=np.percentile(chi_p_INC_10, 95)
INC_10_lower_90=np.percentile(chi_p_INC_10, 5)

chi_p_INC_20 = chi_p_3()
INC_20_upper_90=np.percentile(chi_p_INC_20, 95)
INC_20_lower_90=np.percentile(chi_p_INC_20, 5)

chi_p_INC_30 = chi_p_4()
INC_30_upper_90=np.percentile(chi_p_INC_30, 95)
INC_30_lower_90=np.percentile(chi_p_INC_30, 5)

chi_p_INC_40 = chi_p_5()
INC_40_upper_90=np.percentile(chi_p_INC_40, 95)
INC_40_lower_90=np.percentile(chi_p_INC_40, 5)

chi_p_INC_50 = chi_p_6()
INC_50_upper_90=np.percentile(chi_p_INC_50, 95)
INC_50_lower_90=np.percentile(chi_p_INC_50, 5)

chi_p_INC_60 = chi_p_7()
INC_60_upper_90=np.percentile(chi_p_INC_60, 95)
INC_60_lower_90=np.percentile(chi_p_INC_60, 5)

fig = plt.figure()
ax1 = fig.add_subplot(431)
ax1.hist(chi_p_INC_0,50, facecolor='g', normed=True)

ax1.axvline(x=INC_0_upper_90,linewidth=2,linestyle='dashed',color='k')
ax1.axvline(x=INC_0_lower_90,linewidth=2,linestyle='dashed',color='k')
ax1.axvline(x=inj_v,linewidth=2, color='r')
ax1.set_title('Inclination 0.0 deg')


ax2 = fig.add_subplot(432)
ax2.hist(chi_p_INC_10,50, facecolor='g', normed=True)

ax2.axvline(x=INC_10_upper_90,linewidth=2,linestyle='dashed',color='k')
ax2.axvline(x=INC_10_lower_90,linewidth=2,linestyle='dashed',color='k')
ax2.axvline(x=inj_v,linewidth=2, color='r')
ax2.set_title('Inclination 10.0 deg')

ax3 = fig.add_subplot(433)
ax3.hist(chi_p_INC_20,50, facecolor='g', normed=True)

ax3.axvline(x=INC_20_upper_90,linewidth=2,linestyle='dashed',color='k')
ax3.axvline(x=INC_20_lower_90,linewidth=2,linestyle='dashed',color='k')
ax3.axvline(x=inj_v,linewidth=2, color='r')
ax3.set_title('Inclination 20.0 deg')

ax4 = fig.add_subplot(434)
ax4.hist(chi_p_INC_30,50, facecolor='g', normed=True)

ax4.axvline(x=INC_30_upper_90,linewidth=2,linestyle='dashed',color='k')
ax4.axvline(x=INC_30_lower_90,linewidth=2,linestyle='dashed',color='k')
ax4.axvline(x=inj_v,linewidth=2, color='r')
ax4.set_title('Inclination 30.0 deg')

ax5 = fig.add_subplot(435)
ax5.hist(chi_p_INC_40,50, facecolor='g', normed=True)

ax5.axvline(x=INC_40_upper_90,linewidth=2,linestyle='dashed',color='k')
ax5.axvline(x=INC_40_lower_90,linewidth=2,linestyle='dashed',color='k')
ax5.axvline(x=inj_v,linewidth=2, color='r')
ax5.set_title('Inclination 40.0 deg')

ax6 = fig.add_subplot(436)
ax6.hist(chi_p_INC_50,50, facecolor='g', normed=True)

ax6.axvline(x=INC_50_upper_90,linewidth=2,linestyle='dashed',color='k')
ax6.axvline(x=INC_50_lower_90,linewidth=2,linestyle='dashed',color='k')
ax6.axvline(x=inj_v,linewidth=2, color='r')
ax6.set_title('Inclination 50.0 deg')

ax7 = fig.add_subplot(437)
ax7.hist(chi_p_INC_60,50, facecolor='g', normed=True)

ax7.axvline(x=INC_60_upper_90,linewidth=2,linestyle='dashed',color='k')
ax7.axvline(x=INC_60_lower_90,linewidth=2,linestyle='dashed',color='k')
ax7.axvline(x=inj_v,linewidth=2, color='r')
ax6.set_title('Inclination 60.0 deg')

ax.set_xlabel('chi_p')
ax.set_ylabel('probability density')


plt.savefig("chi_mix_plot2.png")

