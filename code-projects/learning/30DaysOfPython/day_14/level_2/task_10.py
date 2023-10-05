#!/usr/bin/python3
"""Use reduce to sum all the numbers in the numbers list."""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def add(a, b):
    return a + b

sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)
