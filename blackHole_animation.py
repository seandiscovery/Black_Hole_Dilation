import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.cm as cm
from matplotlib.colors import LightSource

from time_dilation import sch_rad, grav_dilation, lorentz_dilation, lorentz_grav_dilation 

"""
Defines plotting and animation functions to demonstrate various properties of Schwarzschild black holes (SBH). 
"""

# global convenience function to convert solar masses to kg
def solarMass_to_kg(solar_mass):
    return solar_mass*2e30 

class dilation_surface(object):

	def __init__(self, solar_mass, time_interval, multiplier, beta_low, beta_high):

		"""
		Initialization for a time dilation surface object. Defines the parameters necessary to plot the surface giving the 
		time dilation of some interval time_interval, for particle travelling radially outside a SBH. 
		Parameters: 
			- solar_mass: mass of black hole, in solar masses
			- time_interval: time interval of dilation 
			- multiplier: defines the default range of radius, from sch rad to multiplier * sch rad 
			- beta_low, beta_high: maximum, minimum speeds to plot 
		"""

		self.solar_mass = solar_mass
		self.time_interval = time_interval
		self.multiplier = multiplier
		self.beta_low = beta_low
		self.beta_high = beta_high
		# compute black hole mass in kg 
		self.hole_mass = solarMass_to_kg(self.solar_mass)
		# compute sch radius 
		self.s_rad = sch_rad(self.hole_mass)

	def plot(self):
		"""
		Plots dilation of interval time_interval against beta and radius 
		"""
		epsilon = 1e-3 # for numeric stability 

		beta = np.linspace(self.beta_low, self.beta_high)
		radius = np.linspace(self.s_rad + epsilon, self.multiplier*self.s_rad)

		fig = plt.figure()
		ax = fig.gca(projection='3d') 
		beta, radius = np.meshgrid(beta, radius)
		dil = lorentz_grav_dilation(beta, self.time_interval, self.s_rad, radius)

		grav_colors = cm.jet(dil)
		grav_surf = ax.plot_surface(beta, radius, dil, facecolors=grav_colors,
		                       linewidth=0, antialiased=True)

		# optional: add a colorbar 
		#sm = cm.ScalarMappable(cmap=cm.coolwarm)
		#sm.set_array(dil)
		#fig.colorbar(sm)

		fig.set_size_inches(8,6)
		plt.show()

	def mass_animation(self, mass_multiplier, iterations, time_step): 
		"""
		Produces a simple animation of how the dilation surface changes as the mass of the black hole changes. 
		Currently, the solar mass scales exponentially with the number of iterations; e.g., on iteration i we have 
		solar_mass = solar_mass_0 * (multiplier)**i, where solar_mass_0 is the original solar mass at iteration 0
		Inputs: 
			- mass_multiplier: the base in multiplier**i 
			- iterations: total number of iterations to run the simulation 
			- time_step: time step for each frame, in seconds. Total time (in sec) for simulaiton 
			  is iterations*time_step 
		"""
		epsilon = 1e-3 # for numeric stability 

		fig = plt.figure()
		ax = fig.gca(projection='3d') 

		# number of iterations 
		its = iterations
		# initialize sch radius (since it changes w/mass)
		s_rad = self.s_rad

		# basic animation loop 
		for i in range(its): 
			# beta, radius grids 
			beta = np.linspace(0.0, 0.9)
			radius = np.linspace(s_rad + epsilon, self.multiplier*s_rad)
			beta, radius = np.meshgrid(beta, radius)

			dil = lorentz_grav_dilation(beta, self.time_interval, s_rad, radius)

			grav_colors = cm.jet(dil)
			grav_surf = ax.plot_surface(beta, radius, dil, facecolors=grav_colors,
		                           linewidth=0, antialiased=True)

			plt.pause(time_step)
		    
			# recompute BH mass / s_rad 
			hole_mass = solarMass_to_kg(self.solar_mass*(self.multiplier)**i)
			s_rad = sch_rad(hole_mass)

	def window_animation(self, window_range, iterations, time_step):
		"""
		A simple animation that shows how the dilation surface changes as the minimum and maximum radii of interest change. 
		Inputs: 
			- window_range: sets the width of window, in units of the Sch radius. In other words, if we set window_range = 10, 
			  the radius axis will have a range (s_rad, 10*s_rad) --> (10*s_rad, 20*s_rad) --> ... 
			  --> (10*(iterations - 1)*s_rad, 10*iterations*s_rad) 
			- iterations, time_step: same as above. Note that iterations sets the maximum radius considered in the animation: 
			  max_radius = iterations*window_range*s_rad  
		"""

		epsilon = 1e-3 # for numeric stability 

		fig = plt.figure()
		ax = fig.gca(projection='3d') 

		# number of iterations 
		its = iterations
		# initialize min, max radius 
		rad_min = self.s_rad + epsilon
		rad_max = window_range*self.s_rad

		# basic animation loop 
		for i in range(its): 
			# beta, radius grids 
			beta = np.linspace(0.0, 0.9)
			radius = np.linspace(rad_min, rad_max) 
			beta, radius = np.meshgrid(beta, radius)

			dil = lorentz_grav_dilation(beta, self.time_interval, self.s_rad, radius)

			grav_colors = cm.jet(dil)
			grav_surf = ax.plot_surface(beta, radius, dil, facecolors=grav_colors,
		                           linewidth=0, antialiased=True)

			plt.pause(time_step)

			# update rad_min, rad_max 
			rad_min = rad_max 
			rad_max = window_range*(i + 1)*rad_max

	def twoD_mass_animation(self, beta, fixed_radius_range, solar_masses, time_step):
		"""
		A simple animation showing how the plot of black hole mass vs time dilation changes 
		as the considered distance from the Sch radius changes 
		Inputs: 
			- beta: velocity of particle 
			- fixed_radius_range: some range of numbers to multiply the minimum Sch radius (corresponding to minimum mass given 
			  in solar_masses) to give the radial distance of the particle at that time step. 
			- solar_masses: range of solar masses considered for the black hole 
			- time_step: same as above 
		"""
		# determine appropriate Sch radii 
		mass = solarMass_to_kg(solar_masses)
		s_rad = sch_rad(mass)

		# main animation loop 
		for r in fixed_radius_range: 
			radius = r*s_rad[0] # in units of Sch radius 
			plt.plot(solar_masses, lorentz_grav_dilation(beta, self.time_interval, s_rad, radius))
			plt.xlabel("Black Hole Mass, solar masses", size=17)
			plt.ylabel("Particle Rest-frame Interval, seconds", size=15)

			plt.pause(time_step)
				    
		   
