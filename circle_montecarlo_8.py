# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:44:12 2020

@author: Jay
"""

import numpy as np
import matplotlib.pyplot as plt
from math import gamma
pi = np.pi

n=10000
global x
x=np.zeros((10,n))

def volume_true_dball(d):
    return (pi**(d/2))/gamma(d/2 + 1)

def volume_MC_dball(d,n):
    
    for i in range(d):
        x[i] = np.random.uniform(-1,1,n)
    
    p=0
    for i in range(n):
        r2 = 0
        for j in range(d):
            r2 = r2 + x[j][i]**2
        if(r2 <=1):
            p=p+1
    
    return (p/n)*(2**d)

d = [2,10]                               #enter no. of dimensions of sphere
vol = [volume_MC_dball(di,n) for di in d]

for i in range(np.size(d)):
    print("Numerically determined volume of",d[i],"dim unit sphere is ",vol[i])
    print("True volume of",d[i],"dim sphere is ",volume_true_dball(d[i]))
    print("******   ******   ******   ******   ******   ******   ******   ******   ******")

plt.figure(figsize=(6,6))
plt.plot(x[0],x[1],'b.',label='MC points')
circle1=plt.Circle((0,0),1,color='r')
plt.gcf().gca().add_artist(circle1)
plt.legend()
plt.title("Area of 2-dim sphere using Monte Carlo; n=10000")
plt.show()