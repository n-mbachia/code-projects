#!/usr/bin/python3
"""Write a function which checks if all the items of the list are of the same data type."""

def is_same_type(list1):
    type1 = type(list1[0])
    for item in list1:
        if type(item) != type1:
            return False
    return True
list1 = [1, 2, 3, 4, 5]

is_same = is_same_type(list1)

if is_same:
  print("All items in the list are of same data type.")
else:
  print("There are different data types on the list.")
