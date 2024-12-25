# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:21:04 2024

@author: DELL E5430
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(11) # using arange to create array "x"
y = x ** 2 # computing square of "x"

# Step 1:
# Creating Figure Object (empty canvas)
fig1 = plt.figure()
# Figure object is created

# Step 2:
# Add axes to the figure object "fig1" -- obj.add_axes()
# [left, bottom, width, height] (range 0 to 1)
axes = fig1.add_axes([0.1, 0.1, 0.9, 0.9]) #Actually positioning our plot on output screen

# Step 3:
# Plotting the data on the set of axes we have created -- axes.plot()
axes.plot(x, y, 'b')

# We can add labels and titles as well! 
# Calling methods to set labels, titles etc -- axes.set....()
axes.set_xlabel('X Label') # Notice the use of set_ to begin methods
axes.set_ylabel('y Label')
axes.set_title('Figure Title') # put ";" if you don't want to see the line of text below!
plt.show()