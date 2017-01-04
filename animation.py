#!/usr/bin/env python3

# Imports
from random import shuffle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bubble_sort import bubble_sort

# Creating the figure and setting up the axes
fig = plt.figure(num=None, figsize=(16, 9), dpi=80, facecolor='w', edgecolor='k')
fig.canvas.set_window_title('Bubble Sort Animation')
ax = fig.add_subplot(1, 1, 1)

# Initializing xs to be an ordered list from 0 to 99
# and ys to be the same list but randomized
xs = list(range(99))
ys = list(range(99))
shuffle(ys)

# Function that animates each iteration of the bubble sort algorithm
def animate(i):
	# This is the bubble_sort function coded by the person doing the tutorial
	bubble_sort(ys)
	ax.clear()
	ax.set_xlabel('Position in List')
	ax.set_ylabel('Value')
	ax.plot(xs, ys, 'ro', markersize=8)

# Beginning the animation
ani = animation.FuncAnimation(fig, animate, interval=80)

# Displaying the plot
plt.show()