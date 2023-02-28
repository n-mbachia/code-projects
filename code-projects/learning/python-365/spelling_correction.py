#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel Day 20"""

from textblob import TextBlob

def convert_to_list(string):
    """ Convert a string of space-seperated words to a list of words."""
    return string.split()
    
# Get user input
user_input = input("Enter your word : ")

# Check if input is empty
if not user_input:
    print("Error: Please enter a word.")
else:
    # Convert input to list of words
    words = convert_to_list(user_input)

    # Correct each word and store in a list
    corrected_words = [str(TextBlob(word).correct()) for word in words]

    #Print output 
    print("Original000 words :", " ".join(words))
    print("Corrected words:", " ".join(corrected_words))

