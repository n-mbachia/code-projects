#!/usr/bin.python3

"""This code is adopted from Python Coding YouTube channel day 11"""

import random # generates characters randomlyex
import string 
import os

passlen = int(input("Enter the legth of desired password : "))

# String storing lowercase, uppercase, digits and special characters
s = string.ascii_letters + string.digits +string.punctuation

p = "".join(random.sample(s,passlen))
""" 'random.sample()' function used to select number of characters randomly from the string. The 'join()' method concatenate the selected characters into a single string"""

# Prompt user to name output file based on what password is for
filename = input("Enter a name for the output file: ")

# Allows errors handling to avoid crashing
try:
    with open(filename,'w') as file: # created file in current directory
        file.write(p) # Write method passed to file
        print("Password written to file:", filename) 
        # Output file can be accessed using 'cat <filename>' on terminal.
 
except OSError as e:
    print("Error writing to file:", e)

