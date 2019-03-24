# Alexandra Macuga, 2019-03-24
# Write a program that outputs whether or not today is a day that begins with the letter T.
# Adapted from: https://web.microsoftstream.com/video/cd3347c4-8296-4e8c-bb63-01ef5452de17

# Import today's date
import datetime

# Check, if is today Tuesday or Thursday
if (datetime.datetime.today().weekday() == 1) or (datetime.datetime.today().weekday() == 3):
  # When the previous if statement is true- today is Tuesday or Thursday, print the specified message to the screen
  print("Yes - today begins with a T.")

#When the previous if statement is false- today is not Tuesday or Thursday, print the specified message to the screen
else:
  print("No - today does not begin with a T.")