# Alexandra Macuga, 2019-03-27
# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.
# Adapted from: https://web.microsoftstream.com/video/b8925ffa-0cf5-4fff-bfb0-b4664f704879

# Import datetime module
import datetime
# Return the current local date and time
datetime.datetime.now()

# Print the formatted date and time
print(datetime.datetime.strftime(datetime.datetime.now(), "%A, %B %dth %Y at %I:%M%p"))