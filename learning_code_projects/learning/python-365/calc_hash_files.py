#!/usr/bin/python3
"""This code was adopted from Python coding Youtube channel day 53..."""

import hashlib

BLOCKSIZE = 65536

def calculate_file_hash(file_path):
    """Function takes file path as arguments and returns a message digest 5 hash file"""
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file: # open file in binary mode
            buf = file.read(BLOCKSIZE) # reads block of data from file
            while len(buf) > 0: # loop iterates till no more data to be read
                hasher.update(buf) 
                buf = file.read(BLOCKSIZE)
        return hasher.hexdigest() # returns MD5 hash file
    except FileNotFoundError:
        return None
    
file_path = "/users/mbachia/code-projects/learning/python-365/age_calc.py"
file_hash = calculate_file_hash(file_path)

if file_hash:
    print("MD5 hash:", file_hash)
else:
    print("File does not exist")
