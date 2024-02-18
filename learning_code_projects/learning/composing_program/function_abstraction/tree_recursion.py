#!/usr/bin/python3

n = int(input("Enter any whole number: "))

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

result = fib(n)

print(f"The", n, "Fibonacci number is", result)
