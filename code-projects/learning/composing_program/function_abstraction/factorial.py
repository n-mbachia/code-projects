#!/ usr/bin/python3

n = int(input("Please enter a whole number: "))
"""Iterative approach"""
def fact_iter(n):
    """Fucntion that takes a single parameter"""
    total, k = 1, 1 # base case set to 1 by tuple unpacking
    while k <= n: # loop True  as long as k is less than or equal to n
        total, k = total * k, k + 1
        """Calculates factorial by mutliplying 'total' by 'k' and then updating the values ot 'total' and 'k' to their new values."""
    return total

result = fact_iter(n)

print(f"Using iterative approach, the factorial of", n, " is: ", result)

"""Recurisve approach"""
def fact(n):
    """Function that takes a single argument"""
    if n == 1: # If True returns 1
         return n
    else: # runs is value of n is False above
         return n * fact(n -1) # multiplies 'n' by all the values of 'n -1' returned by the recusrive call effectively calculating 'n!'.

result = fact(n)

print(f"Using the recursive approach, the factorials of", n, " is: ", result)
