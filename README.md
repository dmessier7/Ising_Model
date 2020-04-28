# Ising_Model
 
Purpose:

## Files
The MetroSim.py file contains the functions for running the Metropolis Algorithm and for storing its results in a csv file.
Functions:
Calc(lattice): Calculate the Energy and Magnetization of a lattice.
 Parameters: 
   lattice - nparray of the lattice
 Returns: Energy, Magnetization
 
func(steps, size, T): Metropolis Algorithm returning a finalized lattice
 Parameters:
     steps - number of steps the metropolis algorithm goes through
     size - edge length of the lattice (e.g. 10 would gives square lattice of 100 sites)
     T - temperature for which the algorithm runs at
 Returns: lattice that is an nparray
 
 funcList(steps, size, T): Metropolis Algorithm returning lists of the Energy and Magnetization after each step
  Parameters:
     steps - number of steps the metropolis algorithm goes through
     size - edge length of the lattice (e.g. 10 would gives square lattice of 100 sites)
     T - temperature for which the algorithm runs at
  Returns: Energy, Magnetization as lists
  
AVG(runs, steps, size, T): Find the average Energy and Magnetization of finalized lattices over a number of runs
 Parameters:
    runs - the number of runs from which the average is taken
    steps - number of steps the metropolis algorithm goes through
    size - edge length of the lattice (e.g. 10 would gives square lattice of 100 sites)
    T - temperature for which the algorithm runs at 
  Returns: Epo, Ene, Mpo, Mne
    Epo - Average of the positive energy values
    Ene - Average of the positive energy values
    Mpo - Average of the positive magnetization values
    Mne - Average of the negative magnetization values
    
store(L, stps, temprange, n): creates a csv in the current directory with n finalized lattices of edge length L for each value in the temprange.
 Parameters:
    L - edge length
    stps - number of steps taken by each run
    temprange - a list of float temperatures
    n - the number of runs for each temperature value from temprange
    
   
