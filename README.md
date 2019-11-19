# monte_carlo_simulation_imf

## A Monte Carlo simulation of a stellar cluster based on the mass distribution at birth, called the Initial Mass Function (IMF)

Stars never form alone, but in clusters with tens to millions of members. A star formation
event produces a population of stars which all have the same birth-time and age, but a range
of different masses.

The distribution of masses which stars have at birth is called the *Initial Mass Function* (IMF). The
IMF can be thought of as a probability distribution which tells you likely a given star born
in a star-formation event is to lie within a particular range of masses. The IMF seems to be
a universal function - it appears to be same everywhere in the Universe and for most of its
history. Determining the IMF is thus a crucially important task.

There are several possible models for the IMF. The simplest and still one of the most popular
is the *Salpeter model*, devised by Edwin Salpeter in 1955. The Salpeter IMF is a single power
law, such that the numbers of stars dN in the mass range M to M+dM is proportional to
$$M^{-2.35}$$.

As well as the slope, one needs to know the upper and lower limits of the mass function.
For the purposes of this project, we assume that the smallest stars have masses of 0.1 solar masses
and that the largest have masses of 100 solar masses. The IMF slope and mass limits completely define the IMF.

In this project we use Monte Carlo methods to make a population of $$10^4$$ or $$10^5$$ stars with
this mass function and plot the distribution of stellar masses as a histogram on log-log
axes. The noise $$Delta N$$ on a histogram bin with N stars in it is $$sqrt(N)$$. 
These results will be later used to extract only certain stars from the cluster that satisfy specific 
distance requirements, and to fit the slope of the mass function using the `numpy polyfit` function.
