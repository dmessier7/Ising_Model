# Ising_Model
 
Purpose: To explore concepts of Statistical Physics and tools in Data Science through the Ising Model.

## Files
### Notebooks
<dl> 
 <dt>GraphingMetroSim</dt>
 <dd>This notebook demonstrates the functions in the MetroSim.py file to ensure their functionality. Including a graph of the Magnetization/site change over temperature.</dd>
 <dt>PCA_sklearn</dt>
 <dd>This notebook uses Principal Component Analysis, a linear dimensional reduction of data, to observe the three possible states of an Ising Lattice: polarized up spin, polarized down spin, and unpolarized.</dd>
 <dt>T-SNE_sklearn</dt>
 <dd>This notebook demonstrates T-SNE, a nonlinear dimensional reduction of data, to visualize the three possible states of an Ising Lattice: polarized up spin, polarized down spin, and unpolarized.</dd>
 <dt>PerceptronModel</dt>
 <dd>This notebook demonstrates a simple linear neural network with an input later, one hidden layer of perceptrons, and an output layer.</dd>
 <dt>ConvolutionNN</dt>
 <dd>This notebook is to demonstrate a convolutional neural network that predicts the whether an Ising Model lattice was simulated below or above the Curie Temperature.</dd>
 </dl>
 
### Reference Files

<dl>
 <dt>MetroSim.py</dt>
 <dd>This file contains the functions for running the Metropolis Algorithm and for storing its results in a csv file.</dd>
 </dl>
 
### CSVs

<dl>
 <dd>Data sets are kept in csv files for further analysis. The naming scheme: edgeLength_NumberOfSteps_RunsPerTemperature.csv</dd>
 </dl>

## Function Documentation
### The MetroSim.py 
<dl>
<dt>Calc(lattice): Calculate the Energy and Magnetization of a lattice.</dt>
 <dd>Parameters:
   lattice - nparray of the lattice
 Returns: Energy, Magnetization</dd></dt>
 
<dt>func(steps, size, T): Metropolis Algorithm returning a finalized lattice</dt>
 <dd>Parameters:
     steps - number of steps the metropolis algorithm goes through
     size - edge length of the lattice (e.g. 10 would gives square lattice of 100 sites)
     T - temperature for which the algorithm runs at
 
 
 Returns: lattice that is an nparray</dd></dt>
 
 <dt>funcList(steps, size, T): Metropolis Algorithm returning lists of the Energy and Magnetization after each step</dt>
  <dd>Parameters:
     steps - number of steps the metropolis algorithm goes through
     size - edge length of the lattice (e.g. 10 would gives square lattice of 100 sites)
     T - temperature for which the algorithm runs at
 
 
  Returns: Energy, Magnetization as lists</dd></dt>
  
<dt>AVG(runs, steps, size, T): Find the average Energy and Magnetization of finalized lattices over a number of runs</dt>
 <dd>Parameters:
    runs - the number of runs from which the average is taken
    steps - number of steps the metropolis algorithm goes through
    size - edge length of the lattice (e.g. 10 would gives square lattice of 100 sites)
    T - temperature for which the algorithm runs at </dd>
 
 
  Returns: Epo, Ene, Mpo, Mne
    Epo - Average of the positive energy values
    Ene - Average of the positive energy values
    Mpo - Average of the positive magnetization values
    Mne - Average of the negative magnetization values</dd></dt>
    
<dt>store(L, stps, temprange, n): creates a csv in the current directory with n finalized lattices of edge length L for each value in the temprange.</dt>
<dd> Parameters:
    L - edge length
    stps - number of steps taken by each run
    temprange - a list of float temperatures
    n - the number of runs for each temperature value from temprange</dd></dt>
</dl>  
   
