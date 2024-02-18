#!/usrs/bin/python3
"""Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list."""

def print_list(list_1):
    """a function with single parameter"""
    for i in list_1:
        print(i) # prints current element in the list
    return(list_1) # returns list from the parameter
print_list([1, 2, 3, 4, 5]) # list of integers
print()
print_list(['Julius', 'Brian', 'Mwangi', 'Kamau', 'Joseph']) # prints a string
