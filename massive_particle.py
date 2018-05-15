"""
The massive_particle class is designed to model a massive particle traveling at some radius r from the event horizon of a Schwarzschild black hole. 

This will be useful when we start constructing a simple black hole simulation tool. 
"""
import numpy as np 

class Massive_Particle(object):

	def __init__(self, M, r, beta):
		"""
		Construct a particle with mass m, radial distance from black hole EH r, and speed beta = v/c --> 0 < beta < 1 
		"""
		self.velocity = beta
		self.radius = r
		self.mass = M 