# Alexandra Macuga, 2019-03-26
# Write a program that takes a user input string and outputs every second word.
# Adapted from: https://stackoverflow.com/a/54857233

# Ask the user for a sentence
s = input("Please enter a sentence: ")
# Split the current sentence by spaces, then take every other word from it
words = s.split()[::2]
# Take the words, separate them by space and join them into the new sentence
s = " ".join(words)
# Print the new sentence
print(s)