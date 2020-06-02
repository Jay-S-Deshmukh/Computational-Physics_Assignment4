# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:51:23 2020

@author: Jay
"""

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.axes.Axes import set_xlabel, set_ylabel

def uniform_3_7(x):
    
    if(x>3 and x<7):
        return 1
    else: return 1e-307

nsteps = 100000
n_bins = 20
theta = 5.0
sample = []
mc = []

for i in range(nsteps):
    theta_prime = theta + np.random.standard_normal()
    mc.append(theta_prime)
    r = np.random.rand()
    
    if(uniform_3_7(theta_prime)/uniform_3_7(theta) > r):
        theta = theta_prime
        
    sample.append(theta)

sample_final = [sample[i] for i in range(50,np.size(sample))]

n1, bins1, patches1 = plt.hist(sample_final, n_bins, facecolor='blue',density='true', alpha=0.5, label='MCMC')
#plt.axhline(y=0.25, xmin=0, xmax=1, hold=None,label='Uniform')
plt.title("MCMC; n=100000")
plt.legend(bbox_to_anchor=(1, 1))
plt.show()

n_mc_arr=[100,1000]

for n_mc in n_mc_arr:
    narr=np.arange(0, n_mc)
    mc_accepted =[sample[i] for i in range(0,n_mc)]
    mc_all =[mc[i] for i in range(0,n_mc)]   
    
    plt.scatter(narr,mc_all)
    plt.plot(mc_accepted,'r',label='Accepted')
    plt.xlabel("Steps")
    plt.ylabel("Theta")
    plt.legend()
    plt.title("Markov Chain: First "+str(n_mc)+" steps")
    plt.show()