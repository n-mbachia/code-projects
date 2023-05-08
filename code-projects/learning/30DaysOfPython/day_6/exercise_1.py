#!/usr/bin/python3
"""Exercise to practise what has been learned on day 6"""

#Level 1

# create and empty tuple
empty_tuple = tuple()
print(f'This is an empty tuple, {tuple()}')

# tuple containing names of brothers
brothers = ('Kama', 'Dennis', 'Cliff')
print(f'The names of my brothers, {brothers}')

# tuple conatining names of sisters
sisters = ('Irene', 'Grace', 'Emelda')

# join sister and brother tuple
siblings = brothers + sisters
print(f'The names of my sisters,{sisters}')

# determine length of Siblings tuple
print(f'The total number of sinlings is, {len(siblings)}')

# Modify siblings by adding parents names
parent_names = list(siblings)
parent_names.append('Joseph')
parent_names.append('Naomy')
family_members = tuple(parent_names)
print(f'The name of my family members, {family_members}')

# Level 2
# create tuples and join them
fruits = ('Melon', 'Apple', 'Pineapple', 'Banana')
vegetables = ('Kales', 'Spinach', 'Brocolli', 'Tomatoes')
animal_products = ('Beef', 'Chicken', 'Turkey', 'Choven')
food_stuff_tp = fruits + vegetables + animal_products
print(f'A tuple containing various food stuffs; {food_stuff_tp}')

# convert tuple to list
food_stuff_lst = list(food_stuff_tp)
print(f'A tuple converted in to a list{food_stuff_lst}/n')

# check it item exists in tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
