#!/usr/bin/python3
"""Use map to create a new list by changing each country to uppercase in the countries list."""
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries_upper = map(lambda country: country.upper(), countries)
print(list(countries_upper))
