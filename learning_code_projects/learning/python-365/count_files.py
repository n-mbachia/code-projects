#!/usr/bin/python3
"""The following code was adopted from Python Coding YouTube channel day 52 ..."""

import os

PATH = "/users/mbachia/code-projects/learning"
file_count = 0
dir_count = 0

for root, dirs, files, in os.walk(PATH):
    print('Looking in:', root)
    for directories in dirs:
        dir_count += 1
    for Files in files:
        file_count += 1

print('Number of files found', file_count)
print('Number of Directories found', dir_count)
print('Total files and directories is:', (dir_count+ file_count))
