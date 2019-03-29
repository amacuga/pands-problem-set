# Alexandra Macuga, 2019-03-29
# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.
# Adapted from: https://stackoverflow.com/a/30551984

# Import module sys
import sys
# Open file from an argument on the command line in the read mode
with open(sys.argv[-1], 'r') as f:
    # Set the value of count to 0 (initialize it)
    count = 0
    # For a line from the file
    for l in f:
        # New value of count is current value of count + 1 (increment by 1 each time the loop is executed)
        count += 1
        # If count is even number
        if count % 2 == 0:
            # Print the line
            print(l)








