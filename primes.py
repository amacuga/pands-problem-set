# Alexandra Macuga, 2019-03-26
# Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
# Adapted from: https://web.microsoftstream.com/video/3ef695e3-9155-4487-b48e-0867834c76ad

# Ask the user for a value of i (positive integer)
i = int(input('Please enter a positive integer: '))

# For a number in a range from 2 to i (positive integer specified by user)
for n in range(2, i):
  # Check if integer is divisible by a number from a range
  if i % n == 0:
    # If an integer is divisible by the number, print the specified message
    print('That is not a prime')
    # When the condition is true and the integer is divisible by at least one number, break the loop
    break
# If the integer is not divisible by any number from a range 
else:
  # Loop fell through without finding a factor, print the specified message
  print('That is a prime.')