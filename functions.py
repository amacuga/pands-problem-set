# Alexandra Macuga, 2019-03-31
# Write a program that displays a plot of the functions x, x^2 and 2^x in the range [0, 4].
# Adapted from: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/ and https://matplotlib.org/users/pyplot_tutorial.html

# Import the specified modules 
import matplotlib.pyplot as plt
import numpy as np

# Return an array with 4 values (stop value is 4)
x = np.arange(4)
# Define values for y1, y2, y3
y1 = x
y2 = x**2
y3 = 2**x

# Plotting the line 1 points
plt.plot(x, y1, label = "x")

# Plotting the line 2 points
plt.plot(x, y2, label = "x^2")

# Plotting the line 3 points
plt.plot(x, y3, label = "2^x")

# Show a legend on the plot
plt.legend()

# Show the plot
plt.show()