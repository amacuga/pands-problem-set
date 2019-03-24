# Alexandra Macuga, 2019-03-24
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.
# Adapted from: https://web.microsoftstream.com/video/82894055-5147-487d-ab35-6bf5c51cd889

# Ask the user for a value of i (positive integer)
i = int(input('Please enter a positive integer: '))

# Print the value of i without newline
print(i, end = ' ')

# While i is more than one
while i > 1:

  # If i is even number (divisible by two)
  if i % 2 == 0:
    # Divide the current value of i by two
    i = (i // 2)
    # And print the new value of i without newline
    print(i, end = ' ')

  # Else if i is odd number (not divisible by two)
  else:
    # Multiply the current value of i by three and add one
    i = (i * 3 + 1)
    # And print the new value of i without newline
    print(i,end = ' ')