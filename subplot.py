import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

print "Initialising..."

injected_value=0.5

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
    
chi_p_INC_0.0 = chi_p_1()
chi_p_INC_10.0 = chi_p_2()
chi_p_INC_20.0 = chi_p_3()
chi_p_INC_30.0 = chi_p_4()
chi_p_INC_40.0 = chi_p_5()
chi_p_INC_50.0 = chi_p_6()
chi_p_INC_60.0 = chi_p_7()
