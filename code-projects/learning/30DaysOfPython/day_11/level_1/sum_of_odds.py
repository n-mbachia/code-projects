#!/usr/bin/python3
"""Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range."""
def sum_of_odds(nums):
    sum_odd = 0
    for num in range(nums):
        if num % 2 != 0:
            sum_odd += num
    return sum_odd
print(sum_of_odds(10))
    
