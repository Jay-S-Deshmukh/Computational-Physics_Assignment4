# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:59:58 2020

@author: Jay
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def exp_pdf(x):
    return 2*np.exp(-2*x)
    

n = 10000
n_bins = 20
x_array = np.linspace(0,5,50)

Y=[]
with open('pdf_exp.txt','r') as file:
    data = csv.reader(file, delimiter=' ')
    for val in data:
        Y.append(float(val[0]))
 
Y = np.array(Y)

n1, bins1, patches1 = plt.hist(Y, n_bins, facecolor='blue', density='true', alpha=0.5, label='Sample')
plt.plot(x_array,exp_pdf(x_array),'r',label='PDF')
plt.title("p(x) = 2e^(-2x)")
plt.axvline(Y.mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(Y.mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(Y.mean()))
plt.legend()
plt.show()