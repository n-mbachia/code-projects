#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 51..."""

def sieve_off(n):
    primes = [True] * (n +1)
    p = 2 #smallest prime number is 2
    while (p * p <= n): 
        if primes[p] == True: #test true for prime number only
            for i in range (p *2, n + 1, p): # marks all mutiples of numbers as False
                primes[i] = False
        p += 1 

    for i in range(2, n): #prints all prime numbers
        if primes[i]:
            print(i)
if __name__ == '__main__':
    n = int(input("Enter a no to check all smaller prime numbers: "))
    sieve_off(n)
