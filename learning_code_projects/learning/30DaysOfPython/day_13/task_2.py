#!/usr/bin/python3
"""Flatten the following list of lists of lists to a one dimensional list"""

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [element for list1 in list_of_lists for list2 in list1 for element in list2]

print(flattened_list)
