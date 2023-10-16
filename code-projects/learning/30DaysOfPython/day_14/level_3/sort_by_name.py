#!/usr/bin/python3

import countries_data

# Sort countries by name. 
countries_by_name = sorted(countries_data.countries, key=lambda c:c["name"])

# Sort countries by capital.
countries_by_capital = sorted(countries_data.countries, key=lambda c: c["capital"])

# Sort countries by population. 
countries_by_population = sorted(countries_data.countries, key=lambda c: c["population"])

# Print the sorted countries. 
print("Countries sorted by name:")
for country in countries_by_name:
    print(country["name"])

print("Countries sorted by capital:")
for country in countries_by_capital:
    print(country["capital"])

print("Countries sorted by population:")
for country in countries_by_population:
    print(country["name"])

