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
    if not variable_name:
        return False

    if keyword.iskeyword(variable_name):
        return False

    if variable_name[0].isdigit():
        return False

    for char in variable_name:
        if not char.isalnum() and char != "_":
            return false

    return True

is_variable = is_valid_variable("my_varibale")

if is_variable:
    print(f"This is valid variable name. \n")
else:
    print("This is not a valid variable name. \n")
