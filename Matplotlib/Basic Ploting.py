# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:26:36 2024

@author: DELL E5430
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(11) # using arange to create array "x"
y = x ** 2 # computing square of "x"

plt.plot(x, y)

# We can add labels and title
plt.xlabel('X Axis Title')
plt.ylabel('Y Axis Title')
plt.title('Figure/plot Title')
plt.show()

# plt.subplot(nrows, ncols, plot_number)

# For plot on left
plt.subplot(1,3,1) # (131) is same as (1,3,1)
plt.plot(x, y, 'r--') 

# For plot in the middle
plt.subplot(1,3,2)
plt.plot(y, x, 'g*-');

# For the plot on right 
plt.subplot(1,3,3)
plt.plot(x, y, 'r--')
plt.plot(y, x, 'g*-');

# Let's adjust the subplots
plt.tight_layout() # try the same code without tight_layout() and see the difference!
plt.show()