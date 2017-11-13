import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import truediv

print "Initialising..."

injected_value=0.75
injected_q = 4
Incliations = [0,10,20,30,40,50,60,70,80]
#manually set injection value
#two functions for each text.file, allowing the creations for MPE and 90PE parameter
def chi_p_1_MPE():
    data = []
    g = open('40M_q1_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    mean_val_1=np.average(saved_chi_p_1)
    MPE_1 = (abs(mean_val_1 - injected_value) / injected_value) * 100
    return MPE_1

def chi_p_1_90PE():
    data = []
    g = open('40M_q1_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    saved_chi_p_1 = [x[52] for x in data ]
    upper_90_1=np.percentile(saved_chi_p_1, 95)
    mean_val_1=np.average(saved_chi_p_1)
    PE_1 = (abs(upper_90_1 - injected_value) / injected_value) * 100
    return PE_1

def chi_p_2_MPE():
    data = []
    f = open('40M_q1_inc_10.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_2 = [x[52] for x in data ]
    mean_val_2=np.average(saved_chi_p_2)
    MPE_2 = (abs(mean_val_2 - injected_value) / injected_value) * 100
    return MPE_2

def chi_p_2_90PE():
    data = []
    f = open('40M_q1_inc_10.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_2 = [x[52] for x in data ]
    upper_90_2=np.percentile(saved_chi_p_2, 95)
    mean_val_2=np.average(saved_chi_p_2)
    PE_2 = (abs(upper_90_2 - injected_value) / injected_value) * 100
    return PE_2

def chi_p_3_MPE():
    data = []
    f = open('40M_q1_inc_20.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_3 = [x[52] for x in data ]
    mean_val_3=np.average(saved_chi_p_3)
    MPE_3 = (abs(mean_val_3 - injected_value) / injected_value) * 100
    return MPE_3

def chi_p_3_90PE():
    data = []
    f = open('40M_q1_inc_20.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_3 = [x[52] for x in data ]
    upper_90_3=np.percentile(saved_chi_p_3, 95)
    mean_val_3=np.average(saved_chi_p_3)
    PE_3 = (abs(upper_90_3 - injected_value) / injected_value) * 100
    return PE_3

def chi_p_4_MPE():
    data = []
    f = open('40M_q1_inc_30.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_4 = [x[52] for x in data ]
    mean_val_4=np.average(saved_chi_p_4)
    MPE_4 = (abs(mean_val_4 - injected_value) / injected_value) * 100
    return MPE_4

def chi_p_4_90PE():
    data = []
    f = open('40M_q1_inc_30.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_4 = [x[52] for x in data ]
    upper_90_4=np.percentile(saved_chi_p_4, 95)
    mean_val_4=np.average(saved_chi_p_4)
    PE_4 = (abs(upper_90_4 - injected_value) / injected_value) * 100
    return PE_4

def chi_p_5_MPE():
    data = []
    f = open('40M_q1_inc_40.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_5 = [x[52] for x in data ]
    mean_val_5=np.average(saved_chi_p_5)
    MPE_5 = (abs(mean_val_5 - injected_value) / injected_value) * 100
    return MPE_5

def chi_p_5_90PE():
    data = []
    f = open('40M_q1_inc_40.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_5 = [x[52] for x in data ]
    upper_90_5=np.percentile(saved_chi_p_5, 95)
    mean_val_5=np.average(saved_chi_p_5)
    PE_5 = (abs(upper_90_5 - injected_value) / injected_value) * 100
    return PE_5

def chi_p_6_MPE():
    data = []
    f = open('40M_q1_inc_50.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_6 = [x[52] for x in data ]
    mean_val_6=np.average(saved_chi_p_6)
    MPE_6 = (abs(mean_val_6 - injected_value) / injected_value) * 100
    return MPE_6

def chi_p_6_90PE():
    data = []
    f = open('40M_q1_inc_50.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_6 = [x[52] for x in data ]
    upper_90_6=np.percentile(saved_chi_p_6, 95)
    mean_val_6=np.average(saved_chi_p_6)
    PE_6 = (abs(upper_90_6 - injected_value) / injected_value) * 100
    return PE_6

def chi_p_7_MPE():
    data = []
    f = open('40M_q1_inc_60.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_7 = [x[52] for x in data ]
    mean_val_7=np.average(saved_chi_p_7)
    MPE_7 = (abs(mean_val_7 - injected_value) / injected_value) * 100
    return MPE_7

def chi_p_7_90PE():
    data = []
    f = open('40M_q1_inc_60.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_7 = [x[52] for x in data ]
    upper_90_7=np.percentile(saved_chi_p_7, 95)
    mean_val_7=np.average(saved_chi_p_7)
    PE_7 = (abs(upper_90_7 - injected_value) / injected_value) * 100
    return PE_7

def chi_p_8_MPE():
    data = []
    f = open('40M_q1_inc_70.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_8 = [x[52] for x in data ]
    mean_val_8=np.average(saved_chi_p_8)
    MPE_8 = (abs(mean_val_8 - injected_value) / injected_value) * 100
    return MPE_8

def chi_p_8_90PE():
    data = []
    f = open('40M_q1_inc_70.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_8 = [x[52] for x in data ]
    upper_90_8=np.percentile(saved_chi_p_8, 95)
    mean_val_8=np.average(saved_chi_p_8)
    PE_8 = (abs(upper_90_8 - injected_value) / injected_value) * 100
    return PE_8

def chi_p_9_MPE():
    data = []
    f = open('40M_q1_inc_80.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_9 = [x[52] for x in data ]
    mean_val_9=np.average(saved_chi_p_9)
    MPE_9 = (abs(mean_val_9 - injected_value) / injected_value) * 100
    return MPE_9

def chi_p_9_90PE():
    data = []
    f = open('40M_q1_inc_80.txt', 'r')
    for line in f:
        data.append([float(x) for x in line.split()])
    saved_chi_p_9 = [x[52] for x in data ]
    upper_90_9=np.percentile(saved_chi_p_9, 95)
    mean_val_9=np.average(saved_chi_p_9)
    PE_9 = (abs(upper_90_9 - injected_value) / injected_value) * 100
    return PE_9

inj_v=0.75

# functions for chi_p histogram

def chi_p_1():
    data = []
    g = open('40M_q1_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_1 = [x[52] for x in data ]
    return Chi_p_1 

def chi_p_2():
    data = []
    g = open('40M_q1_inc_10.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_2 = [x[52] for x in data ]
    return Chi_p_2     

def chi_p_3():
    data = []
    g = open('40M_q1_inc_20.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_3 = [x[52] for x in data ]
    return Chi_p_3 

def chi_p_4():
    data = []
    g = open('40M_q1_inc_30.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_4 = [x[52] for x in data ]
    return Chi_p_4 

def chi_p_5():
    data = []
    g = open('40M_q1_inc_40.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_5 = [x[52] for x in data ]
    return Chi_p_5    

def chi_p_6():
    data = []
    g = open('40M_q1_inc_50.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_6 = [x[52] for x in data ]
    return Chi_p_6 

def chi_p_7():
    data = []
    g = open('40M_q1_inc_60.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_7 = [x[52] for x in data ]
    return Chi_p_7    

def chi_p_8():
    data = []
    g = open('40M_q1_inc_70.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_8 = [x[52] for x in data ]
    return Chi_p_8 

def chi_p_9():
    data = []
    g = open('40M_q1_inc_80.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    Chi_p_9 = [x[52] for x in data ]
    return Chi_p_9

# fuctions for m1

def m1_1():
    data = []
    g = open('40M_q1_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_1 = [x[28] for x in data ]
    return m1_1 

def m1_2():
    data = []
    g = open('40M_q1_inc_10.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_2 = [x[28] for x in data ]
    return m1_2     

def m1_3():
    data = []
    g = open('40M_q1_inc_20.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_3 = [x[28] for x in data ]
    return m1_3 

def m1_4():
    data = []
    g = open('40M_q1_inc_30.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_4 = [x[28] for x in data ]
    return m1_4 

def m1_5():
    data = []
    g = open('40M_q1_inc_40.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_5 = [x[28] for x in data ]
    return m1_5    

def m1_6():
    data = []
    g = open('40M_q1_inc_50.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_6 = [x[28] for x in data ]
    return m1_6 

def m1_7():
    data = []
    g = open('40M_q1_inc_60.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_7 = [x[28] for x in data ]
    return m1_7    

def m1_8():
    data = []
    g = open('40M_q1_inc_70.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_8 = [x[28] for x in data ]
    return m1_8 

def m1_9():
    data = []
    g = open('40M_q1_inc_80.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m1_9 = [x[28] for x in data ]
    return m1_9

#functions for m2

def m2_1():
    data = []
    g = open('40M_q1_inc_0.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_1 = [x[31] for x in data ]
    return m2_1 

def m2_2():
    data = []
    g = open('40M_q1_inc_10.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_2 = [x[31] for x in data ]
    return m2_2     

def m2_3():
    data = []
    g = open('40M_q1_inc_20.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_3 = [x[31] for x in data ]
    return m2_3 

def m2_4():
    data = []
    g = open('40M_q1_inc_30.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_4 = [x[31] for x in data ]
    return m2_4 

def m2_5():
    data = []
    g = open('40M_q1_inc_40.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_5 = [x[31] for x in data ]
    return m2_5    

def m2_6():
    data = []
    g = open('40M_q1_inc_50.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_6 = [x[31] for x in data ]
    return m2_6 

def m2_7():
    data = []
    g = open('40M_q1_inc_60.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_7 = [x[31] for x in data ]
    return m2_7    

def m2_8():
    data = []
    g = open('40M_q1_inc_70.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_8 = [x[31] for x in data ]
    return m2_8 

def m2_9():
    data = []
    g = open('40M_q1_inc_80.txt', 'r')
    for line in g:
        data.append([float(x) for x in line.split()])
    m2_9 = [x[31] for x in data ]
    return m2_9
#manually set injection value

chi_p_INC_0 = chi_p_1()
chi_p_INC_10 = chi_p_2()
chi_p_INC_20 = chi_p_3()
chi_p_INC_30 = chi_p_4()
chi_p_INC_40 = chi_p_5()
chi_p_INC_50 = chi_p_6()
chi_p_INC_60 = chi_p_7()
chi_p_INC_70 = chi_p_8()
chi_p_INC_80 = chi_p_9()


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

#create Mc value
#first line m1 mulitply by m2

m1m2_INC_0 = np.muiltiply(m1_INC_0, m2_INC_0)
m1m2_INC_10 = np.muiltiply(m1_INC_10, m2_INC_10)
m1m2_INC_20 = np.muiltiply(m1_INC_20, m2_INC_20)
m1m2_INC_30 = np.muiltiply(m1_INC_30, m2_INC_30)
m1m2_INC_40 = np.muiltiply(m1_INC_40, m2_INC_40)
m1m2_INC_50 = np.muiltiply(m1_INC_50, m2_INC_50)
m1m2_INC_60 = np.muiltiply(m1_INC_60, m2_INC_60)
m1m2_INC_70 = np.muiltiply(m1_INC_70, m2_INC_70)
m1m2_INC_80 = np.muiltiply(m1_INC_80, m2_INC_80)

m1_m2_INC_0 = np.add(m1_INC_0, m2_INC_0)
m1_m2_INC_10 = np.add(m1_INC_10, m2_INC_10)
m1_m2_INC_20 = np.add(m1_INC_20, m2_INC_20)
m1_m2_INC_30 = np.add(m1_INC_30, m2_INC_30)
m1_m2_INC_40 = np.add(m1_INC_40, m2_INC_40)
m1_m2_INC_50 = np.add(m1_INC_50, m2_INC_50)
m1_m2_INC_60 = np.add(m1_INC_60, m2_INC_60)
m1_m2_INC_70 = np.add(m1_INC_70, m2_INC_70)
m1_m2_INC_80 = np.add(m1_INC_80, m2_INC_80)

TM0 = list(np.array(m1m2_INC_0)**0.6)
TM10 = list(np.array(m1m2_INC_10)**0.6)
TM20 = list(np.array(m1m2_INC_20)**0.6)
TM30 = list(np.array(m1m2_INC_30)**0.6)
TM40 = list(np.array(m1m2_INC_40)**0.6)
TM50 = list(np.array(m1m2_INC_50)**0.6)
TM60 = list(np.array(m1m2_INC_60)**0.6)
TM70 = list(np.array(m1m2_INC_70)**0.6)
TM80 = list(np.array(m1m2_INC_80)**0.6)

LM0 = list(np.array(m1_m2_INC_0)**0.2)
LM10 = list(np.array(m1_m2_INC_10)**0.2)
LM20 = list(np.array(m1_m2_INC_20)**0.2)
LM30 = list(np.array(m1_m2_INC_30)**0.2)
LM40 = list(np.array(m1_m2_INC_40)**0.2)
LM50 = list(np.array(m1_m2_INC_50)**0.2)
LM60 = list(np.array(m1_m2_INC_60)**0.2)
LM70 = list(np.array(m1_m2_INC_70)**0.2)
LM80 = list(np.array(m1_m2_INC_80)**0.2)

Mc_0 = map(truediv, TM0, LM0)
Mc_10 = map(truediv, TM10, LM10)
Mc_20 = map(truediv, TM20, LM20)
Mc_30 = map(truediv, TM30, LM30)
Mc_40 = map(truediv, TM40, LM40)
Mc_50 = map(truediv, TM50, LM50)
Mc_60 = map(truediv, TM60, LM60)
Mc_70 = map(truediv, TM70, LM70)
Mc_80 = map(truediv, TM80, LM80)

# create q values
q_INC_0 = map(truediv, m1_INC_0, m2_INC_0)
q_INC_10 = map(truediv, m1_INC_10, m2_INC_10)
q_INC_20 = map(truediv, m1_INC_20, m2_INC_20)
q_INC_30 = map(truediv, m1_INC_30, m2_INC_30)
q_INC_40 = map(truediv, m1_INC_40, m2_INC_40)
q_INC_50 = map(truediv, m1_INC_50, m2_INC_50)
q_INC_60 = map(truediv, m1_INC_60, m2_INC_60)
q_INC_70 = map(truediv, m1_INC_70, m2_INC_70)
q_INC_80 = map(truediv, m1_INC_80, m2_INC_80)

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

#create q 
q_INC_0_upper_90=np.percentile(q_INC_0, 95)
q_INC_0_lower_90=np.percentile(q_INC_0, 5)
q_0_mean_val_1=np.average(q_INC_0)

q_INC_10_upper_90=np.percentile(q_INC_10, 95)
q_INC_10_lower_90=np.percentile(q_INC_10, 5)
q_10_mean_val_1=np.average(q_INC_10)

q_INC_20_upper_90=np.percentile(q_INC_20, 95)
q_INC_20_lower_90=np.percentile(q_INC_20, 5)
q_20_mean_val_1=np.average(q_INC_20)

q_INC_30_upper_90=np.percentile(q_INC_30, 95)
INC_30_lower_90=np.percentile(q_INC_30, 5)
q_30_mean_val_1=np.average(q_INC_30)

q_INC_40_upper_90=np.percentile(q_INC_40, 95)
q_INC_40_lower_90=np.percentile(q_INC_40, 5)
q_40_mean_val_1=np.average(q_INC_40)

q_INC_50_upper_90=np.percentile(q_INC_50, 95)
q_INC_50_lower_90=np.percentile(q_INC_50, 5)
q_50_mean_val_1=np.average(q_INC_50)

q_INC_60_upper_90=np.percentile(q_INC_60, 95)
q_INC_60_lower_90=np.percentile(q_INC_60, 5)
q_60_mean_val_1=np.average(q_INC_60)

q_INC_70_upper_90=np.percentile(q_INC_70, 95)
q_INC_70_lower_90=np.percentile(q_INC_70, 5)
q_70_mean_val_1=np.average(q_INC_70)

q_INC_80_upper_90=np.percentile(q_INC_80, 95)
q_INC_80_lower_90=np.percentile(q_INC_80, 5)
q_80_mean_val_1=np.average(q_INC_80)

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

q_INC_0_upper_90=np.percentile(q_INC_0, 95)
q_INC_0_lower_90=np.percentile(q_INC_0, 5)
q_0_mean_val_1=np.average(q_INC_0)

q_INC_10_upper_90=np.percentile(q_INC_10, 95)
q_INC_10_lower_90=np.percentile(q_INC_10, 5)
q_10_mean_val_1=np.average(q_INC_10)

q_INC_20_upper_90=np.percentile(q_INC_20, 95)
q_INC_20_lower_90=np.percentile(q_INC_20, 5)
q_20_mean_val_1=np.average(q_INC_20)

q_INC_30_upper_90=np.percentile(q_INC_30, 95)
INC_30_lower_90=np.percentile(q_INC_30, 5)
q_30_mean_val_1=np.average(q_INC_30)

q_INC_40_upper_90=np.percentile(q_INC_40, 95)
q_INC_40_lower_90=np.percentile(q_INC_40, 5)
q_40_mean_val_1=np.average(q_INC_40)

q_INC_50_upper_90=np.percentile(q_INC_50, 95)
q_INC_50_lower_90=np.percentile(q_INC_50, 5)
q_50_mean_val_1=np.average(q_INC_50)

q_INC_60_upper_90=np.percentile(q_INC_60, 95)
q_INC_60_lower_90=np.percentile(q_INC_60, 5)
q_60_mean_val_1=np.average(q_INC_60)

q_INC_70_upper_90=np.percentile(q_INC_70, 95)
q_INC_70_lower_90=np.percentile(q_INC_70, 5)
q_70_mean_val_1=np.average(q_INC_70)

q_INC_80_upper_90=np.percentile(q_INC_80, 95)
q_INC_80_lower_90=np.percentile(q_INC_80, 5)
q_80_mean_val_1=np.average(q_INC_80)

fig = plt.figure()

ax1 = fig.add_subplot(321)
ax1.errorbar(x=Incliations, y=a, yerr=ae, fmt='o', color='g', label = 'Incliation ranges')
ax1.legend(loc='lower right', fontsize=10.5)
ax1.axis([-10, 90, 0, 80])
ax1.set_title('Inclination_scatter_40M_q1_s1x=0.75')
ax1.set_ylabel('Precentage error chi_p (%)', fontsize=12)
ax1.set_xlabel('Inclination (Degrees)', fontsize=12)

ax2 = fig.add_subplot(322)
ax2.plot(Incliations, a, linewidth=2,linestyle='dashed',color='g', label = 'Incliation ranges')
ax2.axis([-10, 90, 20, 80])
ax2.set_title('Inclination_line_40M_q1_s1x=0.75')
ax2.set_ylabel('Precentage error chi_p (%)', fontsize=12)
ax2.set_xlabel('Inclination (Degrees)', fontsize=12)

ax3 = fig.add_subplot(323)
ax3.hist(chi_p_INC_0,50, facecolor='m', normed=True, label = '0 deg')
ax3.hist(chi_p_INC_10,50, facecolor='g', normed=True, label = '10 deg')
ax3.hist(chi_p_INC_20,50, facecolor='b', normed=True, label = '20 deg')
ax3.hist(chi_p_INC_30,50, facecolor='c', normed=True, label = '30 deg')
ax3.hist(chi_p_INC_40,50, facecolor='y', normed=True, label = '40 deg')
ax3.hist(chi_p_INC_50,50, facecolor='grey', normed=True, label = '50 deg')
ax3.hist(chi_p_INC_60,50, facecolor='lightgreen', normed=True, label = '60 deg')
ax3.hist(chi_p_INC_70,50, facecolor='skyblue', normed=True, label = '70 deg')
ax3.hist(chi_p_INC_80,50, facecolor='lightcoral', normed=True, label = '80 deg')
#plt.hist(pycbc_data,50, normed=True, color='b')
ax3.set_xlabel('chi_p')
ax3.axis([0, 1.5, 0, 3])
#plt.axvline(x=Lal_lower_90,linewidth=2,linestyle='dashed',color='m')
#plt.axvline(x=Lal_upper_90,linewidth=2,linestyle='dashed',color='m')
#plt.axvline(x=pycbc_lower_90,linewidth=2,linestyle='dashed',color='k')
#plt.axvline(x=pycbc_upper_90,linewidth=2,linestyle='dashed',color='k')
ax3.axvline(x=inj_v,linewidth=2, color='r')
ax3.set_title('chi_p_histogram_40M_q1_s1x=0.75')
ax3.set_ylabel('probability density')
ax3.legend(loc='upper right', fontsize=10.5)


ax4 = fig.add_subplot(324)
ax4.hist(q_INC_0,50, facecolor='m', normed=True, label = '0 deg')
ax4.hist(q_INC_10,50, facecolor='g', normed=True, label = '10 deg')
ax4.hist(q_INC_20,50, facecolor='b', normed=True, label = '20 deg')
ax4.hist(q_INC_30,50, facecolor='c', normed=True, label = '30 deg')
ax4.hist(q_INC_40,50, facecolor='y', normed=True, label = '40 deg')
ax4.hist(q_INC_50,50, facecolor='grey', normed=True, label = '50 deg')
ax4.hist(q_INC_60,50, facecolor='lightgreen', normed=True, label = '60 deg')
ax4.hist(q_INC_70,50, facecolor='skyblue', normed=True, label = '70 deg')
ax4.hist(q_INC_80,50, facecolor='lightcoral', normed=True, label = '80 deg')
ax4.set_xlabel('q')
ax4.axvline(x=injected_q,linewidth=2, color='r')
ax4.set_title('q_histogram_40M_q4_s1x=0.75')
ax4.set_ylabel('probability density')
ax4.axis([1, 3, 0, 3.5])
ax4.legend(loc='upper right', fontsize=10.5)

ax5 = fig.add_subplot(325)
ax5.errorbar(x=Incliations, y=b, yerr=be, fmt='o', color='g', label = 'Incliation ranges')
ax5.legend(loc='lower right', fontsize=10.5)
ax5.axis([-10, 90, 0, 200])
ax5.set_title('Inclination_scatter_q_40M_q4_s1x=0.75')
ax5.set_ylabel('Precentage error q (%)', fontsize=12)
ax5.set_xlabel('Inclination (Degrees)', fontsize=12)


fig.tight_layout()
fig.set_figheight(15)
fig.set_figwidth(20)




# Set common labels


plt.savefig("Inc_his_q1_7.png")
