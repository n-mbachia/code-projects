#!/usr/bin/python3

"""This code was adopted from Python Coding youTube page day 50..."""

def perfect_number(number):
    sum = 0
    for x in range (1, number):
        if number % x == 0:
            sum += x
    return sum == number

if __name__ == "__main__":
    try:
        n = int(input("Enter a number to check: "))
        result = perfect_number(n)
        if result:
            print(f"You entered the number, {n}, which is a perfect number" )
        else:
            print(f'You entered the number, {n} which is not a perfect number')
    except ValueError:
        print('Invalid input. Please enter a valid integer')             