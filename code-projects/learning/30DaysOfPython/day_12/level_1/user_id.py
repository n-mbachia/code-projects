#!/usr/bin/python3
"""Writ a function which generates a six digit/character random_user_id"""

import random

def random_user_id():
    random_number = random.randint(1000, 999999)
    user_id = str(random_number)
    return user_id

user_id = random_user_id()

print(f"Random generated user id is {user_id}")

