# Alexandra Macuga, 2019-03-24
# Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
# Verbatim from: https://web.microsoftstream.com/video/20963781-2aea-4302-ba73-5b8f327f4189

# Ask the user for a value of i
i = int(input('Please enter a positive integer: '))

# Create a value Total and set it to 0
total = 0

# When the following statement (i is greater than 0) is true, continue and run the following two statements
while i > 0:
    # New value of total is current value of total + i
    total = total + i
    # New value of i is current value of i - 1 (take 1 away from current value of i)
    i = i - 1

# Print the value of total at the end
print(total)