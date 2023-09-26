#!/usr/bin/python3
"""Use filter to filter out countries containing six letters and more in the country list."""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_countries(country):
    if len(country) >= 6:
        return True
    return False

filtered_countries = filter(filter_countries, countries)

print(list(filtered_countries))
