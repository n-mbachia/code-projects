#!/usrs/bin/python3
"""Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range."""

def sum_of_even(nums):
    sum_even = 0
    for num in range(0, nums + 1): # this will include the n-1 item
        if num % 2 == 0:
            sum_even += num
    return sum_even
print(sum_of_even(10))
