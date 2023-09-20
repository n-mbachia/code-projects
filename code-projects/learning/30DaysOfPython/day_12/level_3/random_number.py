#!/usr/bin/python3

import random
def gen_unique_random_numbers(num_of_numbers):
    """Generate a list of unique random numbers in a range of 0 - 9.

    Args:
     num_of_numbers: The number of random numbers to generate. 

    Returns:
     A list of unique random numbers.
    """

    random_numbers = []
    while len(random_numbers) < num_of_numbers:
        random_number = random.randint(0, 9)
        if random_number not in random_numbers:
            random_numbers.append(random_number)

    return random_numbers

# Generate a list of 7 unique random numbers
random_numbers = gen_unique_random_numbers(7)

# Print output
print(random_numbers)
