#!/usrs/bin/python3

"""Compare age to determine who is older or younger"""

your_age = int(input('enter your age: '))
my_age = 34
age_difference = (my_age - your_age)

if my_age > your_age:
    if age_difference == 1:
        print('You are', age_difference, 'year older than me')
    elif age_difference < my_age:
        print('You are', age_difference, 'years younger than me')
    else:
        print('You are', age_difference, 'years older than me')
else:
    if my_age == your_age:
        print('We are the same age')
