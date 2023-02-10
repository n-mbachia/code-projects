#!/usr/bin/python3

tallies = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
# Function with argument
def roman_numeral_to_decimal(romanNumeral):
    # check input using all() function and returns error message if not a roman numeral was entered
    if not all(c in tallies for c in romanNumeral):
        return "Invalid Roman numeral"
    # if single character returns from dictionary
    if len(romanNumeral) == 1:
        return tallies[romanNumeral[0]]

    """create list of pair tuples of adjacent characters from input. 'range(len(romanNumeral) - 1)' expression generates a range of integers from 0 to one less length of 'romanNumeral'. The reason for subtracting 1 from the length of the 'romanNumeral' string is to avoid going out of bounds when accessing the 'i + 1' character in the string."""
    pairs = [(romanNumeral[i], romanNumeral[i + 1]) for i in range(len(romanNumeral) - 1)]
    
    sum = 0
    # iterates through pairs
    for (left, right) in pairs:
        # left value less than right subtract left from sum
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        # left value greater than right, add left to sum
        else:
            sum += tallies[left]
    # add last character to sum and return value
    sum += tallies[romanNumeral[-1]]
    return sum

roman = input("Enter a Roman numeral: ")
# handle lowrcase input using the upper() method 
roman = roman.upper()
# 
result = roman_numeral_to_decimal(roman)
print(result)
