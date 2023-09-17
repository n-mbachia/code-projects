#!/usr/bin/python3
"""Write a function which check if provided variable is a valid python variable"""

import keyword

def is_valid_variable(variable_name):
    """
    Checks if the provided variable ame is a valide Python variable name

    Args:
     variable_name: The variable name to check.

    Returns:
     True if the varibale name is valid, false otherwise. 
    """
    if not variable_name: # checks if empty
        return False

    if keyword.iskeyword(variable_name): # checks if its a Python Keyword
        return False

    if variable_name[0].isdigit(): # checks if the first item is a digit
        return False

    for char in variable_name: # iterates checking for characters
        if not char.isalnum() and char != "_": # checks character for alphanumeric or an underscore
            return False

    return True # proves okay for variable name

is_variable = is_valid_variable("my_varibale") # variable declaired which invokes the function call

# the output is printed as follows
if is_variable:
    print(f"This is valid variable name. \n")
else:
    print("This is not a valid variable name. \n")
