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
ax1 = fig.add_subplot(121)
ax1.hist(chi_p_INC_0,50, facecolor='m', normed=True)

ax1.axvline(x=INC_0_upper_90,linewidth=2,linestyle='dashed',color='m')
ax1.axvline(x=INC_0_lower_90,linewidth=2,linestyle='dashed',color='m')
ax1.axvline(x=inj_v,linewidth=2, color='r')


ax2 = fig.add_subplot(122)
ax2.hist(chi_p_INC_10,50, facecolor='m', normed=True)

ax2.axvline(x=INC_10_upper_90,linewidth=2,linestyle='dashed',color='m')
ax2.axvline(x=INC_10_lower_90,linewidth=2,linestyle='dashed',color='m')
ax2.axvline(x=inj_v,linewidth=2, color='r')


plt.savefig("chi_mix_plot.png")

