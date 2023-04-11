#!/usr/bin/python3
# Day 2: 30 Days of python programming
first_name = 'Mbachia'
last_name = 'Ng\'ethe'
full_name = first_name + last_name
country = 'Kenya'
city = 'Ol kalou'
age = '32'
year = '1989'
is_married = 'Not married'
is_true = 'True'
is_light = 'Dark mode'
first_name, last_name, is_married = 'Mbachia', 'Ng\'ethe', 'Not married'

print(type('Mbachia'))
print(type('Ng\'ethe'))
print(type('Kenya'))
print(type(32))
print(type(1989))
print(type('Not married'))
print(len(first_name))
print(len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
total = num_two - num_one
print(total)
total = num_two * num_one
print(total)
total = num_one / num_two
print(total)
total = num_two % num_one
print(total)
total = num_one ** num_two
print(total)
total = num_one // num_two
print(total)
print()
radius = 30 
area_of_circle = 3.142 * (radius**2)
print(area_of_circle)
circum_of_circle = 2*radius
print(circum_of_circle)

input_radius = int(input("Enter a number: "))
area_of_circle = 3.142 * (input_radius**2)
print(area_of_circle)
circum_of_circle = 2*input_radius
print(circum_of_circle)
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
country = input("Which country are your from?: ")
age = input("Enter your age here: ")

help('keywords')
