#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel day 39..."""

tallies = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,
           'C' : 100, 'D' : 500, 'M' : 1000}
def roman_numeral_to_decimal(roman_numeral):
    total = 0
    for i in range(len(roman_numeral) - 1):
        left = roman_numeral[i]
        right = roman_numeral[i + 1]
        if tallies[left] < tallies[right]:
            total -= tallies[left]
        else:
            total += tallies[left]
    total += tallies[roman_numeral[-1]]
    return total

roman = input("Enter roman number: ")
result = roman_numeral_to_decimal(roman)
print(result)

