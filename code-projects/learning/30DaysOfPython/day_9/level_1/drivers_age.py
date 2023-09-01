#!/usrs/bin/python3
"""This snippet gets user age to determine if they are old enough to drive, 
If not it calculates the difference and lets them know how long they will wait till they can learn to drive"""

drivers_age = int(input('Enter your age: '))
difference = (18 - drivers_age)

if drivers_age >= 18:
    print('You are old enough to learn to drive')
else:
    print('You need', difference, 'more years to learn to drive')
