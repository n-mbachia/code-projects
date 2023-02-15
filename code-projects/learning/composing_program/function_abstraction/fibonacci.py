#!/usr/bin/python3

def fib(n):
    """ Compute the nth fibonacci number, for n >= 2.

    n is enumerator
    k keeps track of created values in loop
    curr is the kth value
    pred is its predecessor
    """
    pred, curr = 0, 1 # Fibonacci numbers 1 and 2
    k = 2 #Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

result = fib(265)
print(result)


