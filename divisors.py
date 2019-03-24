# Alexandra Macuga, 2019-03-24
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
# Adapted from: https://web.microsoftstream.com/video/3ef695e3-9155-4487-b48e-0867834c76ad

# For number between 1,000 and 10,000
for n in range(1000,10000):
  
  #Check if number is divisible by 6 and not divisible by 12
  if n % 6 == 0 and n % 12 != 0:
    # When the previous if statement is true, print the number to the screen
    print(n)