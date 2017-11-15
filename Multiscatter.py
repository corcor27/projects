import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

print "Initialising..."

injected_value=0.75
injected_q = 0.75
injected_Mc = 0.75
Incliations = [0,10,20,30,40,50,60,70,80]
#manually set injection value
#two functions for each text.file, allowing the creations for MPE and 90PE parameter
def chi_p_1_MPE():
    data = []
    g = open('60M_q4_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    mean_val_1=np.average(saved_chi_p_1)
    MPE_1 = (abs(mean_val_1 - injected_value) / injected_value) * 100
    return MPE_1

def chi_p_1_90PE():
    data = []
    g = open('60M_q4_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    upper_90_1=np.percentile(saved_chi_p_1, 95)
    mean_val_1=np.average(saved_chi_p_1)
    PE_1 = (abs(upper_90_1 - injected_value) / injected_value) * 100
    return PE_1

def chi_p_2_MPE():
    data = []
    f = open('60M_q4_inc_10.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_2 = [x[52] for x in data ]
    mean_val_2=np.average(saved_chi_p_2)
    MPE_2 = (abs(mean_val_2 - injected_value) / injected_value) * 100
    return MPE_2

def chi_p_2_90PE():
    data = []
    f = open('60M_q4_inc_10.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_2 = [x[52] for x in data ]
    upper_90_2=np.percentile(saved_chi_p_2, 95)
    mean_val_2=np.average(saved_chi_p_2)
    PE_2 = (abs(upper_90_2 - injected_value) / injected_value) * 100
    return PE_2

def chi_p_3_MPE():
    data = []
    f = open('60M_q4_inc_20.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_3 = [x[52] for x in data ]
    mean_val_3=np.average(saved_chi_p_3)
    MPE_3 = (abs(mean_val_3 - injected_value) / injected_value) * 100
    return MPE_3

def chi_p_3_90PE():
    data = []
    f = open('60M_q4_inc_20.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_3 = [x[52] for x in data ]
    upper_90_3=np.percentile(saved_chi_p_3, 95)
    mean_val_3=np.average(saved_chi_p_3)
    PE_3 = (abs(upper_90_3 - injected_value) / injected_value) * 100
    return PE_3

def chi_p_4_MPE():
    data = []
    f = open('60M_q4_inc_30.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_4 = [x[52] for x in data ]
    mean_val_4=np.average(saved_chi_p_4)
    MPE_4 = (abs(mean_val_4 - injected_value) / injected_value) * 100
    return MPE_4

def chi_p_4_90PE():
    data = []
    f = open('60M_q4_inc_30.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_4 = [x[52] for x in data ]
    upper_90_4=np.percentile(saved_chi_p_4, 95)
    mean_val_4=np.average(saved_chi_p_4)
    PE_4 = (abs(upper_90_4 - injected_value) / injected_value) * 100
    return PE_4

def chi_p_5_MPE():
    data = []
    f = open('60M_q4_inc_40.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_5 = [x[52] for x in data ]
    mean_val_5=np.average(saved_chi_p_5)
    MPE_5 = (abs(mean_val_5 - injected_value) / injected_value) * 100
    return MPE_5

def chi_p_5_90PE():
    data = []
    f = open('60M_q4_inc_40.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_5 = [x[52] for x in data ]
    upper_90_5=np.percentile(saved_chi_p_5, 95)
    mean_val_5=np.average(saved_chi_p_5)
    PE_5 = (abs(upper_90_5 - injected_value) / injected_value) * 100
    return PE_5

def chi_p_6_MPE():
    data = []
    f = open('60M_q4_inc_50.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_6 = [x[52] for x in data ]
    mean_val_6=np.average(saved_chi_p_6)
    MPE_6 = (abs(mean_val_6 - injected_value) / injected_value) * 100
    return MPE_6

def chi_p_6_90PE():
    data = []
    f = open('60M_q4_inc_50.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_6 = [x[52] for x in data ]
    upper_90_6=np.percentile(saved_chi_p_6, 95)
    mean_val_6=np.average(saved_chi_p_6)
    PE_6 = (abs(upper_90_6 - injected_value) / injected_value) * 100
    return PE_6

def chi_p_7_MPE():
    data = []
    f = open('60M_q4_inc_60.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_7 = [x[52] for x in data ]
    mean_val_7=np.average(saved_chi_p_7)
    MPE_7 = (abs(mean_val_7 - injected_value) / injected_value) * 100
    return MPE_7

def chi_p_7_90PE():
    data = []
    f = open('60M_q4_inc_60.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_7 = [x[52] for x in data ]
    upper_90_7=np.percentile(saved_chi_p_7, 95)
    mean_val_7=np.average(saved_chi_p_7)
    PE_7 = (abs(upper_90_7 - injected_value) / injected_value) * 100
    return PE_7

def chi_p_8_MPE():
    data = []
    f = open('60M_q4_inc_70.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_8 = [x[52] for x in data ]
    mean_val_8=np.average(saved_chi_p_8)
    MPE_8 = (abs(mean_val_8 - injected_value) / injected_value) * 100
    return MPE_8

def chi_p_8_90PE():
    data = []
    f = open('60M_q4_inc_70.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_8 = [x[52] for x in data ]
    upper_90_8=np.percentile(saved_chi_p_8, 95)
    mean_val_8=np.average(saved_chi_p_8)
    PE_8 = (abs(upper_90_8 - injected_value) / injected_value) * 100
    return PE_8

def chi_p_9_MPE():
    data = []
    f = open('60M_q4_inc_80.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_9 = [x[52] for x in data ]
    mean_val_9=np.average(saved_chi_p_9)
    MPE_9 = (abs(mean_val_9 - injected_value) / injected_value) * 100
    return MPE_9

def chi_p_9_90PE():
    data = []
    f = open('60M_q4_inc_80.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_9 = [x[52] for x in data ]
    upper_90_9=np.percentile(saved_chi_p_9, 95)
    mean_val_9=np.average(saved_chi_p_9)
    PE_9 = (abs(upper_90_9 - injected_value) / injected_value) * 100
    return PE_9
    
    
def m1_1():
    data = []
    g = open('80M_q4_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_1 = [x[52] for x in data ]
    return m1_1 

def m1_2():
    data = []
    g = open('80M_q4_inc_10.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_2 = [x[52] for x in data ]
    return m1_2     

def m1_3():
    data = []
    g = open('80M_q4_inc_20.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_3 = [x[52] for x in data ]
    return m1_3 

def m1_4():
    data = []
    g = open('80M_q4_inc_30.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_4 = [x[52] for x in data ]
    return m1_4 

def m1_5():
    data = []
    g = open('80M_q4_inc_40.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_5 = [x[52] for x in data ]
    return m1_5    

def m1_6():
    data = []
    g = open('80M_q4_inc_50.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_6 = [x[52] for x in data ]
    return m1_6 

def m1_7():
    data = []
    g = open('80M_q4_inc_60.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_7 = [x[52] for x in data ]
    return m1_7    

def m1_8():
    data = []
    g = open('80M_q4_inc_70.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_8 = [x[52] for x in data ]
    return m1_8 

def m1_9():
    data = []
    g = open('80M_q4_inc_80.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_9 = [x[52] for x in data ]
    return m1_9

#functions for m2

def m2_1():
    data = []
    g = open('M40_INC_0.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_1 = [x[52] for x in data ]
    return m2_1 

def m2_2():
    data = []
    g = open('M40_INC_10.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_2 = [x[52] for x in data ]
    return m2_2     

def m2_3():
    data = []
    g = open('M40_INC_20.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_3 = [x[52] for x in data ]
    return m2_3 

def m2_4():
    data = []
    g = open('M40_INC_30.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_4 = [x[52] for x in data ]
    return m2_4 

def m2_5():
    data = []
    g = open('M40_INC_40.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_5 = [x[52] for x in data ]
    return m2_5    

def m2_6():
    data = []
    g = open('M40_INC_50.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_6 = [x[52] for x in data ]
    return m2_6 

def m2_7():
    data = []
    g = open('M40_INC_60.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_7 = [x[52] for x in data ]
    return m2_7    

def m2_8():
    data = []
    g = open('M40_INC_70.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_8 = [x[52] for x in data ]
    return m2_8 

def m2_9():
    data = []
    g = open('M40_INC_80.0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_9 = [x[52] for x in data ]
    return m2_9
    
m1_INC_0 = m1_1()
m1_INC_10 = m1_2()
m1_INC_20 = m1_3()
m1_INC_30 = m1_4()
m1_INC_40 = m1_5()
m1_INC_50 = m1_6()
m1_INC_60 = m1_7()
m1_INC_70 = m1_8()
m1_INC_80 = m1_9()

m2_INC_0 = m2_1()
m2_INC_10 = m2_2()
m2_INC_20 = m2_3()
m2_INC_30 = m2_4()
m2_INC_40 = m2_5()
m2_INC_50 = m2_6()
m2_INC_60 = m2_7()
m2_INC_70 = m2_8()
m2_INC_80 = m2_9()
    
# recovered values from functions 

run1MPE = chi_p_1_MPE()
run1PE = chi_p_1_90PE()
run2MPE = chi_p_2_MPE()
run2PE = chi_p_2_90PE()
run3MPE = chi_p_3_MPE()
run3PE = chi_p_3_90PE()
run4MPE = chi_p_4_MPE()
run4PE = chi_p_4_90PE()
run5MPE = chi_p_5_MPE()
run5PE = chi_p_5_90PE()
run6MPE = chi_p_6_MPE()
run6PE = chi_p_6_90PE()
run7MPE = chi_p_7_MPE()
run7PE = chi_p_7_90PE()
run8MPE = chi_p_8_MPE()
run8PE = chi_p_8_90PE()
run9MPE = chi_p_9_MPE()
run9PE = chi_p_9_90PE()

# now have values sorted into list

a = [run1MPE,run2MPE,run3MPE,run4MPE,run5MPE,run6MPE,run7MPE,run8MPE,run9MPE]
ae = [run1PE,run2PE,run3PE,run4PE,run5PE,run6PE,run7PE,run8PE,run9PE]

q_INC_0_upper_90=np.percentile(m1_INC_0, 95)
q_INC_0_lower_90=np.percentile(m1_INC_0, 5)
q_0_mean_val_1=np.average(m1_INC_0)

q_INC_10_upper_90=np.percentile(m1_INC_10, 95)
q_INC_10_lower_90=np.percentile(m1_INC_10, 5)
q_10_mean_val_1=np.average(m1_INC_10)

q_INC_20_upper_90=np.percentile(m1_INC_20, 95)
q_INC_20_lower_90=np.percentile(m1_INC_20, 5)
q_20_mean_val_1=np.average(m1_INC_20)

q_INC_30_upper_90=np.percentile(m1_INC_30, 95)
q_INC_30_lower_90=np.percentile(m1_INC_30, 5)
q_30_mean_val_1=np.average(m1_INC_30)

q_INC_40_upper_90=np.percentile(m1_INC_40, 95)
q_INC_40_lower_90=np.percentile(m1_INC_40, 5)
q_40_mean_val_1=np.average(m1_INC_40)

q_INC_50_upper_90=np.percentile(m1_INC_50, 95)
q_INC_50_lower_90=np.percentile(m1_INC_50, 5)
q_50_mean_val_1=np.average(m1_INC_50)

q_INC_60_upper_90=np.percentile(m1_INC_60, 95)
q_INC_60_lower_90=np.percentile(m1_INC_60, 5)
q_60_mean_val_1=np.average(m1_INC_60)

q_INC_70_upper_90=np.percentile(m1_INC_70, 95)
q_INC_70_lower_90=np.percentile(m1_INC_70, 5)
q_70_mean_val_1=np.average(m1_INC_70)

q_INC_80_upper_90=np.percentile(m1_INC_80, 95)
q_INC_80_lower_90=np.percentile(m1_INC_80, 5)
q_80_mean_val_1=np.average(m1_INC_80)

q_MPE_1 = (abs(q_0_mean_val_1 - injected_q) / injected_q) * 100
q_PE_1 = (abs(q_INC_0_upper_90 - injected_q) / injected_q) * 100

q_MPE_2 = (abs(q_10_mean_val_1 - injected_q) / injected_q) * 100
q_PE_2 = (abs(q_INC_10_upper_90 - injected_q) / injected_q) * 100

q_MPE_3 = (abs(q_20_mean_val_1 - injected_q) / injected_q) * 100
q_PE_3 = (abs(q_INC_20_upper_90 - injected_q) / injected_q) * 100

q_MPE_4 = (abs(q_30_mean_val_1 - injected_q) / injected_q) * 100
q_PE_4 = (abs(q_INC_30_upper_90 - injected_q) / injected_q) * 100

q_MPE_5 = (abs(q_40_mean_val_1 - injected_q) / injected_q) * 100
q_PE_5 = (abs(q_INC_40_upper_90 - injected_q) / injected_q) * 100

q_MPE_6 = (abs(q_50_mean_val_1 - injected_q) / injected_q) * 100
q_PE_6 = (abs(q_INC_50_upper_90 - injected_q) / injected_q) * 100

q_MPE_7 = (abs(q_60_mean_val_1 - injected_q) / injected_q) * 100
q_PE_7 = (abs(q_INC_60_upper_90 - injected_q) / injected_q) * 100

q_MPE_8 = (abs(q_70_mean_val_1 - injected_q) / injected_q) * 100
q_PE_8 = (abs(q_INC_70_upper_90 - injected_q) / injected_q) * 100

q_MPE_9 = (abs(q_80_mean_val_1 - injected_q) / injected_q) * 100
q_PE_9 = (abs(q_INC_80_upper_90 - injected_q) / injected_q) * 100

b = [q_MPE_1,q_MPE_2,q_MPE_3,q_MPE_4,q_MPE_5,q_MPE_6,q_MPE_7,q_MPE_8,q_MPE_9]
be = [q_PE_1,q_PE_2,q_PE_3,q_PE_4,q_PE_5,q_PE_6,q_PE_7,q_PE_8,q_PE_9]

#create Mc 

Mc_INC_0_upper_90=np.percentile(m2_INC_0, 95)
Mc_INC_0_lower_90=np.percentile(m2_INC_0, 5)
Mc_0_mean_val_1=np.average(m2_INC_0)

Mc_INC_10_upper_90=np.percentile(m2_INC_10, 95)
MC_INC_10_lower_90=np.percentile(m2_INC_10, 5)
Mc_10_mean_val_1=np.average(m2_INC_10)

Mc_INC_20_upper_90=np.percentile(m2_INC_20, 95)
Mc_INC_20_lower_90=np.percentile(m2_INC_20, 5)
Mc_20_mean_val_1=np.average(m2_INC_20)

Mc_INC_30_upper_90=np.percentile(m2_INC_30, 95)
Mc_INC_30_lower_90=np.percentile(m2_INC_30, 5)
Mc_30_mean_val_1=np.average(m2_INC_30)

Mc_INC_40_upper_90=np.percentile(m2_INC_40, 95)
Mc_INC_40_lower_90=np.percentile(m2_INC_40, 5)
Mc_40_mean_val_1=np.average(m2_INC_40)

Mc_INC_50_upper_90=np.percentile(m2_INC_50, 95)
Mc_INC_50_lower_90=np.percentile(m2_INC_50, 5)
Mc_50_mean_val_1=np.average(m2_INC_50)

Mc_INC_60_upper_90=np.percentile(m2_INC_60, 95)
Mc_INC_60_lower_90=np.percentile(m2_INC_60, 5)
Mc_60_mean_val_1=np.average(m2_INC_60)

Mc_INC_70_upper_90=np.percentile(m2_INC_70, 95)
Mc_INC_70_lower_90=np.percentile(m2_INC_70, 5)
Mc_70_mean_val_1=np.average(m2_INC_70)

Mc_INC_80_upper_90=np.percentile(m2_INC_80, 95)
Mc_INC_80_lower_90=np.percentile(m2_INC_80, 5)
Mc_80_mean_val_1=np.average(m2_INC_80)

Mc_MPE_1 = (abs(Mc_0_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_1 = (abs(Mc_INC_0_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_2 = (abs(Mc_10_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_2 = (abs(Mc_INC_10_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_3 = (abs(Mc_20_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_3 = (abs(Mc_INC_20_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_4 = (abs(Mc_30_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_4 = (abs(Mc_INC_30_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_5 = (abs(Mc_40_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_5 = (abs(Mc_INC_40_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_6 = (abs(Mc_50_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_6 = (abs(Mc_INC_50_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_7 = (abs(Mc_60_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_7 = (abs(Mc_INC_60_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_8 = (abs(Mc_70_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_8 = (abs(Mc_INC_70_upper_90 - injected_Mc) / injected_Mc) * 100

Mc_MPE_9 = (abs(Mc_80_mean_val_1 - injected_Mc) / injected_Mc) * 100
Mc_PE_9 = (abs(Mc_INC_80_upper_90 - injected_Mc) / injected_Mc) * 100

c = [Mc_MPE_1,Mc_MPE_2,Mc_MPE_3,Mc_MPE_4,Mc_MPE_5,Mc_MPE_6,Mc_MPE_7,Mc_MPE_8,Mc_MPE_9]
ce = [Mc_PE_1,Mc_PE_2,Mc_PE_3,Mc_PE_4,Mc_PE_5,Mc_PE_6,Mc_PE_7,Mc_PE_8,Mc_PE_9]

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.errorbar(x=Incliations, y=c, yerr=ce, fmt='o', color='b', label = '40M_q4_inc_40')
ax1.errorbar(x=Incliations, y=a, yerr=ae, fmt='o', color='g', label = '60M_q4_inc_40')
ax1.errorbar(x=Incliations, y=b, yerr=be, fmt='o', color='r', label = '80M_q4_inc_40')
ax1.axis([-10, 90, -35, 35])
ax1.set_title('Inclination_scatter for Chi_p')
ax1.set_ylabel('Precentage error (%)', fontsize=12)
ax1.set_xlabel('Inclination (Degrees)', fontsize=12)
ax1.legend(loc='upper right', fontsize=10.5)

ax2 = fig.add_subplot(122)
ax2.plot(Incliations, c, linewidth=2,linestyle='dashed',color='b', label = '40M_q4_inc_40')
ax2.plot(Incliations, a, linewidth=2,linestyle='dashed',color='g', label = '60M_q4_inc_40')
ax2.plot(Incliations, b, linewidth=2,linestyle='dashed',color='r', label = '80M_q4_inc_40')
ax2.axis([-10, 90, 0, 25])
ax2.set_title('Inclination_line for Chi_p')
ax2.set_ylabel('Precentage error (%)', fontsize=12)
ax2.set_xlabel('Inclination (Degrees)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10.5)

fig.tight_layout()
fig.set_figheight(5)
fig.set_figwidth(10)


# Set common labels


plt.savefig("Multimass_error1.png")
