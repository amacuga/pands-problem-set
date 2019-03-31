# Alexandra Macuga, 2019-03-31
# Write a program that displays a plot of the functions x, x^2 and 2^x in the range [0, 4].
# Adapted from: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/ and https://matplotlib.org/users/pyplot_tutorial.html

# Import the specified modules
import numpy as np
import matplotlib.pyplot as plt

# Return an array with 4 values (stop value is 4)
x = np.arange(4)
# Plotting the line 1 called x
plt.plot(x, x, label = "x")
# Plotting the line 2 called x^2
plt.plot(x, x**2, label = "x^2")
# Plotting the line 3 called 2^x
plt.plot(x, 2**x, label = "2^x")
# Show a legend on the plot 
plt.legend()
# Show the plot
plt.show()