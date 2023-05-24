≈ç\≈çy#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel day 56..."""

import random
import math
lower_value = int(input("Enter lower bound guess value: "))
upper_value = int(input("Enter upper bound guess value: "))

# generate randon number between the two selected bound values
x = random.randint(lower_value, upper_value)
print("\n\tYou've only", round(math.log(upper_value - lower_value + 1, 2)),
      " chances to guess the integer!\n")
# guesses initialized
count_guesses = 0
try:
    # while loop employing boolean type data to test user input
    while count_guesses < math.log(upper_value - lower_value + 1, 2):
        count_guesses += 1
    
        guess_value = int(input("Guess a number between the lower and uper bound values entered: "))
        if x == guess_value:
            print("Congratulations you did it in",count_guesses, " tries")
            break
        elif x > guess_value:
            print("The number you guessed is too small!")
        elif x < guess_value:
            print("The number you guessed is too high!")
    # output based on user success
            if count_guesses >= math.log(upper_value - lower_value + 1, 2):
                print("\nThe number is %d" % x)
except:
                print("\nBetter luck Next Time!")

