#!/usr/bin/python3
"""Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter."""


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def count_by_starting_letter(countries):

    """Counts the number of countries starting with each letter.

    Args:
     countries: A list of country names.

    Returns:
     A dictionary mapping starting letters to counts.
    """

    counts = {}
    for country in countries:
        starting_letter = country[0]
        if starting_letter not in counts:
            counts[starting_letter] = 0
        counts[starting_letter] += 1
    return counts

print(count_by_starting_letter(countries))
