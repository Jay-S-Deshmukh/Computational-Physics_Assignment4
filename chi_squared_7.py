# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:51:50 2020

@author: Dell
"""

import numpy as np
from scipy.stats import chi2

prob_values = [[2,1/36],[3,2/36],[4,3/36],[5,4/36],[6,5/36],[7,6/36],[8,5/36],[9,4/36],[10,3/36],[11,2/36],[12,1/36]]
m = np.shape(prob_values)[0]

data1 = [4,10,10,13,20,18,18,11,13,14,13]
data2 = [3,7,11,15,19,24,21,17,13,9,5]
data = [data1,data2]
k = np.shape(data)[0]

V = [0,0]
cs = [0,0]

for i in range(k):
    n=0
    for j in range(np.size(data[i])):
       n = n + data[i][j]
       
    exp_values = [prob_values[j][1]*n for j in range(m)]
    for j in range(m):
        V[i] = V[i] + ((data[i][j]-exp_values[j])**2)/exp_values[j]
        
    cs[i] = (1.0 - chi2.cdf(V[i],m-1))*100
    
    if(cs[i]<1 or cs[i]>99):
        print("Dataset ",i+1," is not sufficiently random.")
    elif((cs[i]>=1 and cs[i]<=5) or (cs[i]<=99 and cs[i]>=95)):
        print("Dataset ",i+1," is suspect.")
    elif((cs[i]>5 and cs[i]<=10) or (cs[i]<95 and cs[i]>=90)):
        print("Dataset ",i+1," is almost suspect.")
    elif(cs[i]>10 or cs[i]<90):
        print("Dataset ",i+1," is sufficiently random.")
   
   
