#!/usr/bin/python3
"""Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range."""

def sum_of_numbers(nums):
    total = 0
    for num in range(0, nums + 1): # this part of the code ensures that the iteration includes nums-1
        total += num
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
