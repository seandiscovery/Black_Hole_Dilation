import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.cm as cm
from matplotlib.colors import LightSource

from time_dilation import sch_rad, grav_dilation, lorentz_dilation, lorentz_grav_dilation 

"""
This function produces a simple animation showing how the time dilation surface changes as 
a function of the black hole mass. Ultimately, this isn't super interesting, as the surface 
stays more or less constant while the radius axes grows in response to the changing s_rad. 

NOTE: This was a test of the basic animation; this function is included in blackHole_animation.py, wrapped in 
a class for ease of use. 
"""

# convenience function to convert solar masses to kg
def solarMass_to_kg(solar_mass):
    return solar_mass*2e30 

# watch how the time dilation surface changes, as a function of black hole mass 
time_interval = 10 # seconds 
epsilon = 1e-3 # for numeric stability 

fig = plt.figure()
ax = fig.gca(projection='3d') 

# initialize parameters
solar_mass = 0.5
hole_mass = solarMass_to_kg(solar_mass)
s_rad = sch_rad(hole_mass)
# mass multipler 
multiplier = 2
# number of iterations 
its = 10

# basic animation loop 
for i in range(its): 
	# beta, radius grids 
	beta = np.linspace(0.0, 0.9)
	radius = np.linspace(s_rad + epsilon, 10*s_rad)
	beta, radius = np.meshgrid(beta, radius)

	dil = lorentz_grav_dilation(beta, time_interval, s_rad, radius)

	grav_colors = cm.jet(dil)
	grav_surf = ax.plot_surface(beta, radius, dil, facecolors=grav_colors,
                           linewidth=0, antialiased=True)

	plt.pause(0.5)
    
	# recompute BH mass / s_rad 
	hole_mass = solarMass_to_kg(solar_mass*(multiplier)**i)
	s_rad = sch_rad(hole_mass)
	print(hole_mass)
	print(s_rad)
    
