# Alexandra Macuga, 2019-03-31
# Write a program that displays a plot of the functions x, x^2 and 2^x in the range [0, 4].
# Adapted from: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

# Import module
import matplotlib.pyplot as plt 

# Line 1 points 
x1 = [0,1,2,3,4]
y1 = [0,1,2,3,4]
# Plotting the line 1 points  
plt.plot(x1, y1, label = "x") 
  
# Line 2 points 
x2 = [0,1,2,3,4]
y2 = [0,1,4,9,16]
# Plotting the line 2 points  
plt.plot(x2, y2, label = "x^2") 

# Line 3 points 
x3 = [0,1,2,3,4]
y3 = [1,2,4,8,16]
# Plotting the line 3 points  
plt.plot(x3, y3, label = "2^x")
  
# Show a legend on the plot 
plt.legend() 
  
# Show the plot 
plt.show()