"""
Least common multiple (LCM) is a mathematical concept 
referring to the smallest number that the given nu8mbers will all divide into evenly.
This ensure that the result is consistent and efficient

"""

# function defined
def least_common_multiple(a, b):
    # check for greater value of input
    # assign variable as "greater"
    if a > b:
        greater  = a
    elif b > a:
        greater = b
    while (True):
        # checks if the multiple evenly divides 
        if ((greater % a == 0) and (greater % b == 0)):
            # value of lcm equal to "greater"
            lcm = greater
            break #takes program out of infinite loop
        greater = greater + 1 #increment each interation
    return lcm # returns value of lcm

#Accept user input
a = int(input("Enter any number greater than zero: "))
b = int(input("Enter another number greater than zero: "))
print(least_common_multiple(a, b))

"""The least common multiple (LCM) is a mathematical concept that is used in various fields such as mathematics, science, and engineering. LCM has real-life applications, including:
1. Scheduling: To determine the smallest interval that covers all appointments or meeting times.
2. Cryptography: To determine a shared key between two parties.
3. Music theory: To find the smallest common denominator of musical rhythms.
4. Robotics: To synchronize the motion of multiple robots.
"""
