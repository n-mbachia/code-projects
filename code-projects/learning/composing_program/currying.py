#!/usr/bin/python3
"""Explains the currying technique where a function is transofmed into a chain of nested functions each taking a single argument"""

def curried_power(x):
    """ Function takes  a single argument x and returns another funtion h"""
    def h(y):
        """ Function takes  a single argument y and raises 'x' to a power"""
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    """ Funtion takes three arguments: start, end and f to loop over an integer value"""
    while start < end:
        print(f(start)) # calling function f on each value and printing result
        start = start + 1

map_to_range(0, 10, curried_power(2))

"""First we call the curried_power with argument 2 to create a new function 'f' that raises 2 to a power. Then, we call 'map_to_range' with arguments '0', '10' and 'f' which causes it to print the power of 1, 2 to power of 2. and so on up to 2 to the power of 10."""

