# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:45:56 2020

@author: Jay
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner
import csv

def f(x,a,b,c):
    
    return a*x*x + b*x + c

def log_likelihood(theta, x, y, yerr):
    
    a, b, c = theta
    model = a*x*x + b*x + c
    sigma2 = yerr**2
    
    return 0.5*np.sum((y - model)**2/sigma2 +  np.log(2*np.pi*sigma2))

def log_prior(theta):
    
    a, b, c = theta
    
    if(-500.0 < a < 500.0 and -500.0 < b < 500.0 and -500.0 < c < 500.0):
        return 0.0
    return -np.inf

def log_probability(theta, x, y, yerr):
    
    lp = log_prior(theta)
    
    if not np.isfinite(lp):
        return -np.inf
    
    return lp - log_likelihood(theta, x, y, yerr)

x = [] 
y = [] 
sigma_y = []
with open('data.txt','r') as file:
    table = csv.reader(file, delimiter='&')
    for i in range(5): next(table)
    for column in table:
        x.append(float(column[1]))
        y.append(float(column[2]))
        sigma_y.append(float(column[3]))

x = np.array(x)
y = np.array(y)
sigma_y = np.array(sigma_y)
guess = (1.0,1.0,1.0)
soln = minimize(log_likelihood, guess, args=(x, y, sigma_y))

nwalkers, ndim = 50, 3
pos = soln.x + 1e-4*np.random.randn(nwalkers, ndim)
nsteps = 4000

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(x, y, sigma_y))
sampler.run_mcmc(pos, nsteps)
samples = sampler.get_chain()

plt.plot(samples[:,:,0])
plt.title("Markov Chains a: 50 chains, 4000 steps")
plt.xlabel("Steps")
plt.ylabel("a")
plt.show()

plt.plot(samples[:,:,1])
plt.title("Markov Chains b: 50 chains, 4000 steps")
plt.xlabel("Steps")
plt.ylabel("b")
plt.show()

plt.plot(samples[:,:,2])
plt.title("Markov Chains c: 50 chains, 4000 steps")
plt.xlabel("Steps")
plt.ylabel("c")
plt.show()

samples = np.reshape(samples,(nsteps*nwalkers,ndim))
medians = np.median(samples, axis = 0)
a_true, b_true, c_true = medians

h = 0.5
a1 = np.amin(x)
a2 = np.amax(x)
N = int((a2-a1)/h) + 1
xarr = np.linspace(a1,a2,N)
c_no = np.random.randint(0,nsteps*nwalkers,200)
for i in c_no:
    a_c, b_c, c_c = samples[i]
    plt.plot(xarr, f(xarr,a_c,b_c,c_c), 'y')
    
plt.plot(xarr, f(xarr,a_c,b_c,c_c), 'y', label='Candidate Model')
plt.plot(xarr, f(xarr,a_true,b_true,c_true), 'r', label='Best-Fit Model')
plt.errorbar(x, y, sigma_y, marker='s',mfc='black',fmt='ks',label='Data')
plt.title("Models: ax^2 + bx + c")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

fig = corner.corner(samples,  labels=["a","b","c"], show_titles=True, quantiles=[0.16, 0.5, 0.84], truths=[a_true, b_true, c_true])