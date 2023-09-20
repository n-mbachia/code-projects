#!/usrs/bin/python3
"""Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list"""

import random

def shuffle_list(list1):
    """Shuffles a list. 

    Args:
     list1: A list to be shuffled.

     Returns:
      A shuffled list. 
    """

    shuffled_list = list1.copy() # Creates a copy of list argument as passed
    for i in range(len(shuffled_list)): # iterates over elements
        rand_index = random.randint(0, len(shuffled_list) -1) # generates a random index based on length of copy
        shuffled_list[i], shuffled_list[rand_index] = shuffled_list[rand_index], shuffled_list[i] # swaps current element with random index


    return shuffled_list

#Get user input
list1 = ["Kenyatta", "Moi", "Kibaki", "Uhuru", "Ruto"]

random_list = shuffle_list(list1)

print(f"The original list: {list1}.\nThe shuffled list is: {random_list}")
