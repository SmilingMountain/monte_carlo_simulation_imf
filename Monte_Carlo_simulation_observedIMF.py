# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:11:30 2017

@author: ai15aax
"""
# Observed IMF Monte Carlo Simulation

import numpy as np
import matplotlib.pyplot as plt
in_string1=input('Number of stars= ')
n=float(in_string1)
print('Generating stellar cluster...')

def pdf(x,zeta0):
    """
    Probability distribution function used in Salpeter's power law IMF model:
    ξ(M) = ξ0 * M^(−2.35)
    Input: 
    x = mass of the star (M)
    zeta0 = constant which sets the local stellar density (ξ0)
    Output: 
    Initial Mass Function ξ(M)  (IMF) i.e. the number of stars in the cluster
    with masses between M and M + ΔM
    """
    return zeta0*x**(-2)

def randomvariate(pdf,n,xmin,xmax):  
  """  
 Rejection method for random number generation  
 ===============================================  
 Uses the rejection method for generating random numbers derived from an arbitrary   
 probability distribution. 
 Usage:  
 >>> randomvariate(pdf,n,xmin,xmax)  
  where  
  pdf : probability distribution function from which you want to generate random numbers  
  n : desired number of random values  
  xmin,xmax : range of random numbers desired  
 Returns:   
  the sequence (ran,ntrials) where  
   ran : array of shape N with the random variates that follow the input P  
   ntrials : number of trials the code needed to achieve n  
 The algorithm:  
 - generate x' in the desired range  
 - generate y' between Pmin and Pmax (Pmax is the maximal value of your pdf)  
 - if y'<pdf(x') accept x', otherwise reject  
 - repeat until desired number is achieved   
  """  
  # Calculates the minimal and maximum values of the PDF in the desired  
  # interval. The rejection method needs these values in order to work  
  # properly.  
  x=np.linspace(xmin,xmax,n)
  zeta0=(n*1.35)/((xmin)**(-1.35)-(xmax)**(-1.35)) # the zeta0 factor taken from literature  
  y=pdf(x,zeta0)  
  pmin=0.  
  pmax=y.max()  
  # Counters  
  naccept=0  
  ntrial=0  
  # Keeps generating numbers until we achieve the desired n  
  ran=[] # output list of random numbers  
  while naccept<n:  
      x=np.random.uniform(xmin,xmax) # x'  
      y=np.random.uniform(pmin,pmax) # y'  
      if y<pdf(x,zeta0):  
          ran.append(x)  
          naccept=naccept+1  
      ntrial=ntrial+1  
  ran=np.asarray(ran)  
    
  return ran,ntrial
  
result=randomvariate(pdf,n,0.5,150)
cluster=result[0]
print('\n cluster=',cluster)

a=plt.figure(1) # creating the log-log histogram:
counts,bin_edges=np.histogram(cluster,bins=np.logspace(-0.5,2,30))
plt.hist(cluster,range=(-0.5,2.5),bins=np.logspace(-0.5,2,30),log=True)
plt.yscale('log')
plt.xscale('log')
bin_centres=(bin_edges[:-1]+bin_edges[1:])/2. # this calculates the x position of the error bars
err=np.sqrt(counts) # error from Poisson distribution
plt.errorbar(bin_centres,counts,yerr=err,fmt='x') # plotting the error bars

plt.xlabel("$M/M_\odot$")
plt.ylabel("Number of stars")
plt.title("Observed IMF")
plt.savefig("histogram") # saves with extension .png

plt.show()

plt.close()