"""
Defines gravitational time dilation/Lorentz transformations for particle at a relativistic speed near a Schwarzschild black hole. 
"""

import numpy as np 
from scipy import constants

def grav_dilation(hole_mass, radius, far_time):
	"""
	Computes graviational time dilation for a Schwarzschild black hole of mass hole_mass. This function assumes that 
	both observers are along the same radial coordinate extending from the black hole center; far_time is the time interval 
	measured by the observer at radius_far > radius, where radius is the distance of the "closer" observer to the black hole. 
	That is, the observer at radius_far measures a weaker gravitational field than the observer at radius. 

	Note that far_time is a time interval, i.e. far_time = t_1 - t_0 for some even the far observer measures as beginning at t_0 and 
	ending at t_1. 
	"""

	return far_time*np.sqrt(1 - 2*constants.G*hole_mass/(radius*(constants.speed_of_light)**2) )

def lorentz_dilation(beta, time_interval):
	"""
	Computes time dilation due to special relativistic effects: in other words, time dilation due to high velocity (beta --> c). 
	Assumes the time_interval provided is measured in the rest frame of the moving particle.
	"""

	gamma = 1.0/np.sqrt(1 - beta**2)
	return gamma*time_interval

def lorentz_grav_dilation(beta, time_interval, hole_mass, radius):
	"""
	Combines the effects of special and general relativity for a massive particle traveling in the radial direction 
	from a Schw. black hole of mass hole_mass. This can be derived by introducing a non-zero beta into the Schw. metric. 
	"""

	sch_rad = 2*constants.G*hole_mass/(radius*(constants.speed_of_light)**2)
	return time_interval*np.sqrt( (1 - sch_rad/radius)*( 1 - (beta**2)/(1 - sch_rad/radius)**2 ) )

