# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:52:07 2020

@author: Jay
"""
import numpy as np
import matplotlib.pyplot as plt
import time

n = 10000
n_bins = 20
X = np.zeros(n)

a = 1664525
c = 1013904223
m = 2**(32)
X[0] = 1

start = time.time()
for i in range(n-1):
    X[i+1] = (a*X[i] + c)%m

X = X/m
print(time.time() - start)
X_uniform = np.random.random(n)

plt.figure(figsize=(7,7))
n1, bins1, patches1 = plt.hist(X, n_bins, facecolor='blue',density='true', alpha=0.5, label='LCG')
#n2, bins2, patches2 = plt.hist(X_uniform, n_bins, facecolor='red',density='true', alpha=0.5, label='Uniform')
plt.axhline(y=1, xmin=0, xmax=1, hold=None,label='Uniform')
plt.title("Linear Congruential Generator; n=10000")
plt.legend()
plt.show()