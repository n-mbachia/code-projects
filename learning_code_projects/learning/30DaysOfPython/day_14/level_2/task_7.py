#!/usr/bin/python3

"""Use filter to filter out countries starting with an 'E'"""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_char_e(countries):
    country_with_e = []
    for country in countries:
        if country[0] == "E":
            country_with_e.append(country)

    return country_with_e

starting_with_e = filter(None, filter_char_e(countries))

print(list(starting_with_e))
