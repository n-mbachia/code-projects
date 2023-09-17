#!/usr/bin/python3
"""Write a functions which checks if all items are unique in the list."""
def all_unique(list1):
  return len(list1) == len(set(list1))
list1 = [1, 2, 3, 4, 5]

is_unique = all_unique(list1)

if is_unique:
  print("All items in the list are unique.")
else:
  print("There are duplicate items in the list.")
