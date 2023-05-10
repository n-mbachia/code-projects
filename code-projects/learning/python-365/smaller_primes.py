#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 51..."""

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
    return prime_numbers


if __name__ == '__main__':
    n = int(input("Enter a number to check all smaller prime numbers: "))
    primes = sieve_of_eratosthenes(n)
    print("Prime numbers smaller than or equal to", n, ":")
    print(primes)

