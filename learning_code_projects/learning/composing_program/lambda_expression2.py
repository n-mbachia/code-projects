#!/usr/bin/python3
"""This code corrects the spelling of a given text input using the Textblob library"""
from textblob import TextBlob

def compose1(f, g):
    """Funtion that takes two function arguments f and g as inputs."""
    return lambda x: f(g(x))

def correct_spelling(string):
    """Function takes a input string argument and applies the textblob correct() method to each word in string"""
    li = string.split() # 'f' Function splits the string in to a list of words
    corrected_words = [] # Corrected words assigned to this variable
    for word in li:
        # 'g' function applies the correct_spelling() function to each word in the list
        corrected_words.append(str(TextBlob(word).correct()))
    return " ".join(corrected_words) # Returns string using join() method seperated by commas
# Promt user input
str_input = input("Enter a sentence: ")
f = compose1(correct_spelling, lambda x: x) # Lambda function takes a single argument
""" call compose1 with the two lambda functions and assign resulting function to variable f"""
corrected = f(str_input)

# Print output for user
print()

print("Original Sentence: ", str_input)
print("Corrected Sentence: ", corrected)
