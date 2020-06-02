# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:25:48 2020

@author: Jay
"""
import numpy as np
import matplotlib.pyplot as plt
import time

n = 10000
n_bins = 20

start = time.time()
X = np.random.rand(n)
print(time.time() - start)
#X_uniform = np.random.random(n)

plt.figure(figsize=(7,9))
n1, bins1, patches1 = plt.hist(X, n_bins, facecolor='blue', density='true', alpha=0.5, label='Numpy')
#n2, bins2, patches2 = plt.hist(X_uniform, n_bins, facecolor='red', alpha=0.5, label='Uniform')
plt.axhline(y=1, xmin=0, xmax=1, hold=None,label='Uniform')
plt.title("np.random.rand; n=10000")
plt.legend()
plt.show()