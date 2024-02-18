#!/usr/bin/python3
"""Use map to change each name to uppercase in the names list"""

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

names_upper = map(lambda name: name.upper(), names)
print(list(names_upper))
