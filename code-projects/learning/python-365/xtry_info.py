#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel Day 13"""

# pip3 install country info
from countryinfo import CountryInfo

xtry = input("Enter your country : ") # get country name from user

try:
    # Try block retries country info based on input as argument
    country = CountryInfo(xtry)

    # f-string is formatted to include country name and a list based on function call
    print(f"Capital of {xtry} is: {country.capital()}")
    print(f"Currencies used in {xtry} are: {country.currencies()}")
    print(f"Languages spoken in {xtry} are: {country.languages()}")
    print(f"Countries that share a border with {xtry} are: {country.borders()}")
    print(f"Other names for {xtry} are: {country.alt_spellings()}")

# this will be implemented if input is invalid thus program doesn't crash
except KeyError:
    print("Error: Invalid country name entered")
