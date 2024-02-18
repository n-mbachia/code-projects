#!/usr/bin/python3

"""Use filter to filter out countries having exactly six characters."""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filtered_characters(countries):
    if len(countries) == 6:
        return True
    return False

filtered_name = filter(filtered_characters, countries)
print(list(filtered_name))
        
            
