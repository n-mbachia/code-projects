#!/usr/bin/python3
"""Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan'))."""

def categorize_countries(countries, pattern):
    matching_countries = []
    for country in countries:
        if pattern in country:
            matching_countries.append(country)
    return matching_countries

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Icela\
nd']

land_countries = categorize_countries(countries, "land")
ia_countries = categorize_countries(countries, "ia")
island_countries = categorize_countries(countries, "island")
stan_countries = categorize_countries(countries, "stand")

print("Land countries:", land_countries)
print("Ia countries:", ia_countries)
print("Island_countries:", island_countries)
print("Stan_countries:", stan_countries)    
