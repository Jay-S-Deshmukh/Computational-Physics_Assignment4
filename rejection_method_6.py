# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:01:40 2020

@author: Numpy
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    
    return np.sqrt(2/np.pi)*np.exp(-x*x/2)

def g(x):
    
    return 1.5*np.exp(-x)

n = 10000
n_bins = 20

X = np.random.rand(n)
X = -np.log(X)
Y = np.random.rand(n)*g(X)
x = np.linspace(0,10,20)

X_good = []
Y_good = []
for i in range(n):
    if( Y[i] <= f(X[i]) ):
        X_good.append(X[i])
        Y_good.append(Y[i])

X_good = np.array(X_good)

plt.plot(X,Y,'r.')
plt.plot(X_good,Y_good,'g.',label='Accepted')
plt.plot(x,f(x),label='PDF')
plt.plot(x,g(x),label='Envelope')
plt.title("Rejection Method: n = " + str(n))
plt.legend()
plt.show()

plt.plot(x,f(x),label='PDF')
plt.hist(X_good, n_bins, range=(0.0,10.0), density=True,label='Sample')
plt.axvline(X_good.mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(X_good.mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(X_good.mean()))
plt.title("Half-Normal Distribution")
plt.legend()
plt.show()