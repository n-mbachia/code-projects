#!/usr/bin/python3

"""Use map to create a new list by changing each number to its square in the numbers list"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sqr_numbers = map(lambda number: number ** 2, numbers)
print(list(sqr_numbers))
