#!/usr/bin/python3
"""Write a function called is_prime, which checks if a number is prime."""

"""A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. 2 is the only even prime number. """

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1): # iterates from 2 till sq of provided number
        if num % i == 0: # checks if any divide evenly hence returns fasle
            return False

    return True # retruns trie for prime numbers only


user_input = int(input("Enter a number to check if it is a prime number: \n"))

is_prime_result = is_prime(user_input)

if is_prime_result:
    print(f"The number you entered - {user_input} - is a prime number")
else:
    print(f"The number you entered - {user_input} - is not a prime number")
