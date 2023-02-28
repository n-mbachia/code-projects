#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel Day 21."""

import logging
from turtle import *
# Set up logging
logging.basicConfig(filename='spinner.log', level=logging.DEBUG)

# Set up the state dictionary
state = {'rotation_angle': 0}

# Define the spinner function
def spinner():
    """ A function that defines fidget with primary colours that spins to the right"""
    try:
        clear() # function clears the turple canvas
        angle = state['rotation_angle']/10
        right(angle)
        forward(100)
        dot(120, 'red') # Draws the red colored circle or dot
        back(100) # Returns the dot toi initiual position
        right(120) # Rotation direction
        forward(100)
        dot(120, 'yellow') # Draws the yellow dot
        back(100)
        right(120)
        forward(100)
        dot(120, 'blue') # Draws the blue dot
        back(100)
        right(120)
        update() # Function updates the turtle canvas
    except Exception as e:
        logging.exception(f'Error in spinner(): {e}')

# Define the animate function
def animate():
    """ Function animates 'spinner' function and updates rotation angle"""
    try:
        if state['rotation_angle'] > 0: # Check rotation angle
           state['rotation_angle'] -= 1
        spinner() # calls spinner function
        ontimer(animate, 20) # Schedules spinner function to 20 milisecond delay using the ontimer function
    except Exception as e:
        logging.exception(f'Error in spinner(): {e}')

# Define the flick function
def flick():
    """ function updates the rotation angle"""
    state['rotation_angle']+=10
# Turtle window setup
setup(420, 420, 370, 0) # Turtle window width, height, and x-y cordinates 
hideturtle()  
tracer(False)
width(30)

# Key bindings to start animation
onkey(flick, 'space') # Pressing and holding to 'space bar' interacts with fidget
listen()
animate() # Function starts the animation loop 

#Start the turtle main loop
try:
    done()
except Exception as e:
    logging.exception(f'Error in spinner(): {e}')
