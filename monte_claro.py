# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

###########################################################

import numpy as np
import matplotlib.pyplot as plt

def Energy(R,A=1,B=1):
    return((A/R**12)-(B/R**6))
    
rand_no=np.random.uniform(0.8,2)
nos=[]
E = Energy(rand_no)
nos.append(rand_no)
for i in range(10000):
    rand_stepsize=np.random.uniform(-0.05,0.05)
    new_rand_no= rand_no + rand_stepsize
    if Energy(new_rand_no) < E:
        nos.append(new_rand_no)
        rand_no = new_rand_no
        E = Energy(new_rand_no)
        
plt.plot(nos,Energy(np.array(nos)))
plt.show()

print("Minimum Enegy at (SimpleMC) : ",nos[np.argmin(Energy(np.array(nos)))])

rand_no=np.random.uniform(0.8,2)
nos=[]
E = Energy(rand_no)
nos.append(rand_no)

for i in range(100):
    rand_stepsize=np.random.uniform(-0.05,0.05)
    new_rand_no= rand_no + rand_stepsize
    if np.random.uniform(0,1)<np.exp(-(Energy(new_rand_no) - E)):
        nos.append(new_rand_no)
        rand_no = new_rand_no
        E = Energy(new_rand_no)
        
plt.plot(nos,Energy(np.array(nos)))
plt.show()

print("Minimum Enegy at (MMC): ",nos[np.argmin(Energy(np.array(nos)))])

rand_no=np.random.uniform(0.8,2)
nos=[]
E = Energy(rand_no)
nos.append(rand_no)
T = 100
while T >= 1:
    for i in range(100):
        rand_stepsize=np.random.uniform(-0.5,0.5)
        new_rand_no= rand_no + rand_stepsize
        if np.random.uniform(0,1)<np.exp(-((Energy(new_rand_no) - E))/T):
            nos.append(new_rand_no)
            rand_no = new_rand_no
            E = Energy(new_rand_no)
    T = 0.9 * T
plt.plot(nos,Energy(np.array(nos)))
plt.show()

print("Minimum Enegy at (Simulated Annealing): ",nos[np.argmin(Energy(np.array(nos)))])