#!/usr/bin/python3

tallies = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
# Function with argument
def roman_numeral_to_decimal(romanNumeral):
    """ function to evaluate user input using the argument passed as romanNumeral
"""
    if not all(c in tallies for c in romanNumeral):
        return "Invalid Roman numeral"
    if len(romanNumeral) == 1: # handles single character input
        return tallies[romanNumeral[0]]

    """create list of pair tuples of adjacent characters from input. 'range(len(romanNumeral) - 1)' expression generates a range of integers from 0 to one less length of 'romanNumeral'. The reason for subtracting 1 from the length of the 'romanNumeral' string is to avoid going out of bounds when accessing the 'i + 1' character in the string."""
    pairs = [(romanNumeral[i], romanNumeral[i + 1]) for i in range(len(romanNumeral) - 1)]
    
    sum = 0
    for (left, right) in pairs: # iterate through pairs
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left] # add last character to sum and return value
    sum += tallies[romanNumeral[-1]]
    return sum

roman = input("Enter a Roman numeral: ")
roman = roman.upper() # method handles case sensitivty error 
result = roman_numeral_to_decimal(roman) # stores value evaluated
print(result)
