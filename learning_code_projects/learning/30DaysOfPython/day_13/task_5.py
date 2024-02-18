#!/usr/bin/python3
"""Change the following list to a list of dictionaries"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_data = [{'country': country_name, 'city': capital_city} for country in countries for country_name, capital_city in country]

print(country_data)

"""This code works by first iterating over the list of countries and the sublist within each country. For each country, the code then creates a new dictionary containing the country name and the capital city.

Finally, the new dictionary is added to the country_data list."""
