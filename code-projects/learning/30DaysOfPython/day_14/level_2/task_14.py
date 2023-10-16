#!/usr/bin/python3
"""Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder."""

import os

def get_first_ten_countries():
    """Returns a list of the first ten coubntries from the countries.py in the data folder.
     
    Args:
     A list of the first ten countries.

    Returns:
     A list of first ten countries. 
    """

    # Get the path to the countries.py file.
    countries_path = os.path.join(os.path.dirname(__file__), "countries.py")
    
    # Open the countries.py file and read the list of countries.
    with open(countries_path, "r") as f:
        countries = f.readlines()
    
    
    # Remove the whitespace from each name.
    countries = [country.strip() for country in countries]

    # Return the firt ten countries.
    return countries[:10]

first_ten_countries = get_first_ten_countries()
print(first_ten_countries)

