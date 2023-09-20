#!/usr/bin/python3
"""Write a function list_of_rgb_colors which returns any number of RGB colors in an array."""
import random

def list_of_rgb_colors(num_of_colors):
    """Generates a list of random RGB colors.

    Args:
     num_of_colors: The number of RGB colors to generate.

    Returns:
     A list of RGB colors.
    """
    
    rgb_colors = []
    for i in range(num_of_colors):
        #Generate a random RGB color
        rgb_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # add the RGB color to list
        rgb_colors.append(rgb_color)
        
    return rgb_colors

#Prompt user input 
user_input = int(input("Enter the number of colors to generate:\n"))

# Function call
generate_array = list_of_rgb_colors(user_input)

# Console output
print(f"The colors required by user are {user_input} and the color codes generated are \n {generate_array}")
