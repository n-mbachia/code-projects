#!/usr/bin/python3
"""Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number."""
 
def evens_and_odds(nums):
    evens = 0
    odds = 0
    for num in range(1, nums + 1):
      if num % 2 == 0:
        evens += 1
      else:
        odds += 1
    return evens, odds
evens, odds = evens_and_odds(100)
print(f"The number of evens are {evens}")
print(f"The number of odds are {odds}")
