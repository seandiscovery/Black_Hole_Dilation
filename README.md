# Modeling relativistic effects near a Schwarzschild black hole #

## Project Overview ##

Explore how gravitational time dilation and time dilation from relativistic speeds interact for a massive particle near a Schwarzschild black hole. 

We compare the following systems: 

-A particle at rest a distance r from the event horizon of a Schw. black hole 

-A particle moving at a relativistic speed in the absence of a gravitational field 

-A particle moving at a radial relativstic speed at an instantaneous distance r from the EH of a Schw. black hole 

The basic code for this comparison is simple, and is included in time_dilation.py. The actual plots are included in both time_dilation_test.ipynb (scratch notebook for developing project) and Physics_91SI_Final_Presentation.ipynb (final notebook for the in-class presentation), both included in the folder Python_Notebooks. 

A class for constructing 3d plots of the time dilation surface near a SBH, as well as basic animations of how this surface changes with various variables, is defined in blackHole_animation.py. Tests of the plotting functions defined in this class are included in the folder Test_Functions. Since animations don't run in Jupyter notebooks, the file presentation_animations.py contains a script to run the relevant animations from the command line. 

NOTE: If you run the code locally, I suggest unpacking all files into one folder. The code has not yet been corrected to account for the new folders Test_Functions and Python_Notebooks; these were included to organize the repository.  

## References ##

Stanford EPGY: https://web.stanford.edu/~oas/SI/SRGR/notes/SRGRLect9B_2013.pdf

Wikipedia: https://en.wikipedia.org/wiki/Schwarzschild_metric, https://en.wikipedia.org/wiki/Time_dilation#cite_note-ashby02-38

Matplotlib docs: https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html, https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

