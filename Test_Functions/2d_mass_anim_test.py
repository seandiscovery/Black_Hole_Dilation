""" 
Test the 2d mass animation funciton in blackHole_animation.py
This animation is included in presentation_animation.py
"""
import numpy as np
import blackHole_animation as BH 

# parameters needed to construct the black hole 
solar_mass = 0.5
time_interval = 10 
multiplier = 10
beta_low = 0.0
beta_high = 0.9

# construct two black hole animation objects (for two animations below)
black_hole_1 = BH.dilation_surface(solar_mass, time_interval, multiplier, beta_low, beta_high)
black_hole_2 = BH.dilation_surface(solar_mass, time_interval, multiplier, beta_low, beta_high)

# test the 2d animation 
beta = 0.5 
# we split the radius range up into two parts, so we don't get too many plots on one graph 
fixed_radius_range_1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]	
fixed_radius_range_2 = [1000, 1500, 2500, 3000, 3500, 4000, 4500, 5000]
solar_masses = np.linspace(1, 1e3, num=1000)
time_step = 1.0

# run the animations 
black_hole_1.twoD_mass_animation(beta, fixed_radius_range_1, solar_masses, time_step)
black_hole_2.twoD_mass_animation(beta, fixed_radius_range_2, solar_masses, time_step)
