#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 34..."""

rows = int(input("Enter a diamond pattern rows: "))
print("Diamond Star Pattern")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end= '')
    for k in range(0, 2 * i - 1):
        print('*', end= '')
    print()
for i in range(1, rows):
    for j in range(1, i + 1):
        print(" ", end= '')
    for l in range(1, (2 * (rows - i) )):
        print('*', end= '')
    print()
