"""Least common multiple (LCM) is a mathematical concept 
referring to the smallest number that the given nu8mbers will all divide into evenly."""


def least_common_multiple(a, b):
    if a > b:
        greater  = a
    elif b > a:
        greater = b
    while (True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm
a = int(input("Enter any number greater than zero: "))
b = int(input("Enter another number greater than zero: "))
print(least_common_multiple(a, b))

"""The least common multiple (LCM) is a mathematical concept that is used in various fields such as mathematics, science, and engineering. LCM has real-life applications, including:
1. Scheduling: To determine the smallest interval that covers all appointments or meeting times.
2. Cryptography: To determine a shared key between two parties.
3. Music theory: To find the smallest common denominator of musical rhythms.

4. Robotics: To synchronize the motion of multiple robots.

In these fields, LCM provides a solution to the problem of finding the smallest number that the given numbers will all divide into evenly. This helps to ensure that the result is consistent and efficient."""
