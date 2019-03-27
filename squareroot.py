# Alexandra Macuga, 2019-03-27
# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.
# Adapted from: https://web.microsoftstream.com/video/dca7ddaa-9512-4810-a758-237921e6440e

# Ask the user for a value of rootof (floating number)
rootof = float(input('Please enter a positive number: '))
# This is the initial estimate for the square root.
estimate = 6.0

# Keep going until the square of estimate is within 0.1 of rootof
while abs((estimate*estimate) - rootof) > 0.1:
  # This is Newton's method to improve our estimate
  estimate -= ((estimate * estimate) - rootof) / (2 * estimate)
# Round the estimate to one decimal place.
estimate = round(estimate, 1)
  
# Print the result
print(f'The square root of {rootof} is approx. {estimate}.')

