import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.cm as cm
from matplotlib.colors import LightSource
#%matplotlib inline

from time_dilation import sch_rad, grav_dilation, lorentz_dilation, lorentz_grav_dilation 

"""
This code plots the time dilation surface for a Schwarzchild black hole. Code identical to that in the 
iPython notebook time_dilation_test.

NOTE: This was a test of the basic function; now included in blackHole_animation.py, wrapped in a class for ease of use.  
"""

# convenience function to convert solar masses to kg
def solarMass_to_kg(solar_mass):
    return solar_mass*2e30 

# 3D plot of lorentz_grav_dilation as a function of beta, radius 
hole_mass = solarMass_to_kg(2) # solar masses 
time_interval = 10 # seconds 
epsilon = 1e-3 # for numeric stability 
print(hole_mass)

beta = np.linspace(0.0, 0.9)
s_rad = sch_rad(hole_mass)
print(s_rad)
radius = np.linspace(s_rad + epsilon, 10*s_rad)

fig = plt.figure()
ax = fig.gca(projection='3d') 
beta, radius = np.meshgrid(beta, radius)
dil = lorentz_grav_dilation(beta, time_interval, s_rad, radius)

grav_colors = cm.jet(dil)
grav_surf = ax.plot_surface(beta, radius, dil, facecolors=grav_colors,
                       linewidth=0, antialiased=True)

# optional: add a colorbar 
#sm = cm.ScalarMappable(cmap=cm.coolwarm)
#sm.set_array(dil)
#fig.colorbar(sm)

fig.set_size_inches(8,6)
plt.show()
