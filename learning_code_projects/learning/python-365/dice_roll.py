#!/usr/bin/python3

import random # module importation
# A dice has 6 phases starting from 1 through 6. 
min_val = 1 
max_val = 6

roll_again = "yes" # variable allows user input to loop, any other they exit loop

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice ...")
    print("The values are : ")

    # from module we are genrating a random whole number
    print(random.randint(min_val, max_val)) # number between defined valuesls

    # Asks uyser to keep rolling dice. 
    roll_again = input("Would you like to roll the dice again?")
