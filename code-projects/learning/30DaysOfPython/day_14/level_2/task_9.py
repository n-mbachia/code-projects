#!/usr/bin/python3
"""Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items."""

def get_string_lists(lst):
    string_list = [x for x in lst if isinstance(x, str)]
    return string_list

lst = [1, 2, 3, 4, "Mwanainchi"]
string_list = get_string_lists(lst)
print(string_list)
