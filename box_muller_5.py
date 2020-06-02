# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:18:01 2020

@author: Jay
"""
import numpy as np
import matplotlib.pyplot as plt

def gauss_pdf(x):
    return np.sqrt(1/(2*np.pi))*np.exp(-x**2/2)

n=10000
n_bins = 20
x_array = np.linspace(-4,4,50)

x1 = np.random.rand(n)
x2 = np.random.rand(n)
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)


n1, bins1, patches1 = plt.hist(y1, n_bins, facecolor='blue', density='true', alpha=0.5, label='Sample')
plt.plot(x_array,gauss_pdf(x_array),'r',label='Gaussian PDF')
plt.axvline(y1.mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(y1.mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(y1.mean()))
plt.title("Box-Muller")
plt.legend()
plt.show()