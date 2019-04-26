# Statistical Mechanics and Computations - Book

Code exercises from the textbook
[*Statistical Mechanics: Algorithms and Computations*](http://blancopeck.net/Statistics.pdf) by *Werner Krauth*.

## 1 Monte Carlo Methods

 * smac.c   Useful functions

### Section 1.1 Popular Games in Monaco
* 1.1 Implement Algorithm 1.1. Plot error and investigate relationship with N.
  * direct-plot.py
* 1.2 Implement Algorithm 1.2. Plot error and rejection rate.
  * markov-pi.py
* 1.3 Store state in file
  * direct.py
  * smacfiletoken.py
* 1.4 Use table
  * markov-discrete-pebble.py
  * large-markov.pi
* 1.8 Eigenvalues of transfer matrix
  * transfer.m
* 1.13 Vectors within Uniform sphere
  * sphere-test.py

### Section 1.2 Basic Sampling
* 1.9 Sample permutations
  * permutation.py    Sample permutations using Alg. 1.11 and verify that it generate all 120 permutaions of 5 elements equally often.
  * permutation-histogram.py

* 1.12 Gauss
  * naivegauss.py
  * boxmuller.py

### Section 1.3 Statistical data analysis
* 1.18 Binomial Convolution
  * binomialconvolution.py

### Section 1.4 Computing

 #### Section 1.4.2 Importance Sampling

 * 1.22 Importance sampling
   * direct-gamma.py  Implement Algorithm 1.29, subtract mean value for each sample, and generate histograms of the average of N samples  and the rescaled averages.
   * direct-gamma-zeta.py
   * markov-zeta.py  Implement Algorithm 1.31, use of Markov Chain to detect non-integrable singularity.
   
 #### Section 1.4.4 Stable Distribution
  * levy-convolution.py  Implement Algorithm 1.32
  
##  2 Hard Disks and Spheres

### Section 2.2 Boltzmann's Statistical Mechanics
 * directDisksAny.py
  
##  2 Hard Disks and Spheres

### Section 2.2 Boltzmann's Statistical Mechanics
 * directDisksAny.py

## 3 Density Matrices and Path Integrals

## 4 Bosons

## 5 Order and disorder in spin systems

### Section 5.1 The Ising model - exact computations

 * gray.py   Algorithm 5.2 gray-flip
 * ising.py  Algorithm 5.3 enumerate-ising. Tested against Table 5.2 4x4 case.
 
## 6 Entropic Forces

## 7 Dynamic Monte Carlo Methods


 
