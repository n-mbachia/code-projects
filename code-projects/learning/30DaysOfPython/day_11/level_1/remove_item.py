#!/usr/bin/python3
"""Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it."""

def remove_item(list1, item):
    list1.remove(item)
    return list1
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))
