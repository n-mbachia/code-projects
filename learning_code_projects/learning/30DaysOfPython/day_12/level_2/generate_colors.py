#!/usr/bin/python3
"""Write a function generate_colors which can generate any number of hexa or rgb colors."""

import random

def generate_colors(num_of_colors, color_type):
    """Generate a list of random colors.
    
    Args:
     num_of_colors: The number of colors to generate.
     color_type: They type of color to generate, either "hexa" or "rgb". 

    Returns:
     a list of colors.
    """

    colors = []
    for i in range(num_of_colors): 
        if color_type == "hexa":
            
            # Generate a random hexadecimal color
            hexa_color = "#"
            for j in range(6):
                rand_num = random.randint(0, 15)
                hexa_color += hex(rand_num)[2:]
            
            # Add the hexadecimal color to the list
            colors.append(hexa_color)
        elif color_type == "rgb":
            
            # generate a random rgb color
            rgb_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            # Add the RGB color to the list
            colors.append(rgb_color)
        else:
            raise ValueError("Invalid color type:{}".format(color_type))
    
    return colors

# get user input here
num_of_colors = int(input("Pleae enter the number of colors to be generated: \n"))
color_type = input("Please enter the color type either 'hexa' or 'RGB': \n")

# Invoke the function 
get_output = generate_colors(num_of_colors, color_type)

# Console output
print(f"The colors code generated is: \n {get_output}")
