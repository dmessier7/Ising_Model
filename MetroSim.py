import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as r
import os

# Constants
J = 1 # Interaction Constant
k = 1 # Scaled Boltzmann Constant


# Set up Lattice with random spins
def Setup(N):
    lattice = np.ones((N,N), dtype=int) # start with all +1
    for x in np.nditer(lattice, op_flags=['readwrite']): # For Loop to random change some to -1
        x[...] = 2*r.randrange(2) - 1
    return lattice

# Calculate the 
def Calc(p):
    En = 0
    M = 0
    i = 0
    while i < np.size(p, 0):
        j = 0
        while j < np.size(p, 1):
            En += ((p[i,j]*p[(i+1)%np.size(p, 0),j]) + (p[i,j]*p[i, (j+1)%np.size(p, 1)]))
            M += p[i,j]
            j += 1
        i += 1
    En *= -J
    return En, M

# Metro Simulation: Output of final lattice
def func(steps, size, T): # Function to run through
    s = 0
    latt = Setup(size) # Set up random lattice of size^2
    while s < steps:
        n, m = r.randrange(0, size, 1), r.randrange(0, size, 1) # two random values for a random location on the lattice
        old  = (latt[(n-1)%size,m]*latt[n,m]) + (latt[(n+1)%size,m]*latt[n,m]) + (latt[n,(m-1)%size]*latt[n,m]) + (latt[n,(m+1)%size]*latt[n,m])
        latt[n,m] *= -1 # try flipping the spin at that site
        new  = (latt[(n-1)%size,m]*latt[n,m]) + (latt[(n+1)%size,m]*latt[n,m]) + (latt[n,(m-1)%size]*latt[n,m]) + (latt[n,(m+1)%size]*latt[n,m])
        de = -J*(new - old) # dE = Ef - Ei
        if de > 0 and r.random() > np.exp(-de/(k*T)):
                latt[n,m] *= -1 # Return the spin to normal if not accepted
        # The lattice wont change back unless the de is positive and the random number is above transition prob
        s += 1
    return latt

# Metro Simulation: Output lists of Energy and Magnetization run
def funcList(steps, size, T): # Function to run through 
    s = 0 
    E = [] # list to store energy initially and after each step 
    M = [] # list to store magentization initially and after each step
    latt = Setup(size) # Set up random lattice of size^2
    g, h = Calc(latt) # Calculate it's initial Energy and Magnetization
    E.append(g) # Store the initial values as 
    M.append(h)
    while s < steps:
        n, m = r.randrange(0, size, 1), r.randrange(0, size, 1) # two random values for a random location on the lattice
        old  = (latt[(n-1)%size,m]*latt[n,m]) + (latt[(n+1)%size,m]*latt[n,m]) + (latt[n,(m-1)%size]*latt[n,m]) + (latt[n,(m+1)%size]*latt[n,m])
        latt[n,m] *= -1 # try flipping the spin at that site
        new  = (latt[(n-1)%size,m]*latt[n,m]) + (latt[(n+1)%size,m]*latt[n,m]) + (latt[n,(m-1)%size]*latt[n,m]) + (latt[n,(m+1)%size]*latt[n,m])
        de = -J*(new - old) # dE = Ef - Ei
        if de > 0: # If there would be more energy in the system if the spin is flipped
            if r.random() < np.exp(-de/(k*T)): # Randomly choose to accept the spin based on the transition prob
                u, c = Calc(latt)
                E.append(u)
                M.append(c)
            else:
                latt[n,m] *= -1 # Return the spin to normal if not accepted
                g = E[-1]
                h = M[-1]
                E.append(g) # still jot down the energy and mag for the step
                M.append(h)
        else: # If there would be less energy in the system with the flipped spin, automatically accept
            u, c = Calc(latt)
            E.append(u)
            M.append(c)
            
        s += 1
    E[:] = [x / (size**2) for x in E] # Energy per site
    M[:] = [x / (size**2) for x in M] # Magnetization per site
    return E, M

# Find Average magnetization and energy for a temperature
def AVG(runs, steps, size, T):
    E = []
    M = []
    i= 0
    while i < runs:
        q = func(steps, size, T)
        h, j = Calc(q)
        E.append(h)
        M.append(j)
        i+=1
    E = sum(E)/len(E)
    Mpos, Mneg=[i for i in M if i>0 ],[j for j in M if j<0] 
    if len(Mpos) != 0:
        Mpo = sum(Mpos)/len(Mpos)
    else:
        Mpo = None
    if len(Mneg) != 0:
        Mne = sum(Mneg)/len(Mneg)
    else:
        Mne = None
    return E, Mpo, Mne

# Store n finalized lattices for a range of tempeatures into a csv
def store(L, stps, tempRange, n): 
    S = ['S'+ str(i) for i in range(L**2)]
    S.insert(0, 'T')
    M = [str(round(i,1))+':'+str(j) for i in tempRange for j in range(n)]
    data = pd.DataFrame(columns=S, index=M)
    for i in tempRange:
        i = round(i,1)
        b = 0
        while b < n:
            m = func(stps, L, i)
            latt = m.flatten()
            latt  = np.concatenate(([i],latt), axis=0)
            data.loc[str(i)+':'+ str(b)] = latt
            b += 1
    p = os.getcwd()
    data.to_csv (r''+p+'/'+str(L)+'_'+str(stps)+'.csv', index = True, header=True)
