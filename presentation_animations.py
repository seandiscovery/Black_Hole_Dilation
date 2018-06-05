import blackHole_animation as BH 

"""
This function instantiates a black hole animation object (defined in the file blackHole_animation.py), and then runs various animations 
detailing how the time dilation surface changes with different variables. 
"""

# parameters needed to construct the black hole 
solar_mass = 2
time_interval = 10 
multiplier = 10
beta_low = 0.0
beta_high = 0.9

# construct a black hole animation object 
black_hole = BH.dilation_surface(solar_mass, time_interval, multiplier, beta_low, beta_high)

# first, we'll plot the basic surface 
black_hole.plot()

# next, we'll produce an animation detailing how the time dilation surface changes as a function 
# of black hole mass 
mass_multiplier = 2
iterations = 10 
time_step = 0.2
# run the animation 
black_hole.mass_animation(mass_multiplier, iterations, time_step)

# what happens if we change the range of radii that our particle could inhabit? 
# let's animate it! 
window_range = 100 
# run the animation 
black_hole.window_animation(window_range, iterations, time_step)

"""
Next, we'll produce an animation of how the (two dimensional) curve of time dilation versus black hole mass changes as we vary 
the radius at which our fixed observer sits.  
"""
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


