#!/usr/bin/python3
"""Use filter to filter out countries containing 'land'."""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_countries(countries):
    """Filteres a list of countries to only include those contaning word land,

    Args:
     countries: A list of string country names,

    Returns:
     A list of string, representing only contries that contain the word land
     """

    filtered_countries = []
    for country in countries:
        if "land" in country.lower():
            # return if True
            filtered_countries.append(country)
        else:
            # return if False
            filtered_countries.append(None)
    # return the list created after running code
    return filtered_countries
# pass filter function to declaired variable
filtered_countries = filter(None, filter_countries(countries))

# outputs to console
print(list(filtered_countries))

