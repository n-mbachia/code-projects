#!/usr/bin/python3
"""Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items"""

def capitalize_list_items(list1):
    """Used to capitalize all items in a list
    Arguments:
    accepts one parameter list1
    Returns:
    A list of capitalized items."""
    for i in range(len(list1)):
        list1[i] = list1[i].capitalize()
    return list1
list1 = ['python', 'java', 'react']
print(capitalize_list_items(list1)) 
        
