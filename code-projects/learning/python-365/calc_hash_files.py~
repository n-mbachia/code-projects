#!/usr/bin/python3
"""This code was adopted from Python coding Youtube channel day 53..."""

import hashlib

BLOCKSIZE = 65536

def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            buf = file.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(BLOCKSIZE)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    
file_path = "/users/mbachia/code-projects/learning/python-365/age_calc.py"
file_hash = calculate_file_hash(file_path)

if file_hash:
    print("MD5 hash:", file_hash)
else:
    print("File does not exist")
    