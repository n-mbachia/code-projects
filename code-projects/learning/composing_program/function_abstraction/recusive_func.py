#!/bin/python3
# Promt user input
n = int(input("Enter any number: "))

def sum_digits(n):
    """Function returns the sum of digits of positive integer n."""
    if n < 10: 
        return n
    else: 
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

result = sum_digits(n)

print(result) 

sum_digits(n) # Function call with user Input as argument

