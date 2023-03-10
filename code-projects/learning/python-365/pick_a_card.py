#!/usr/bin/python3

"""This code was adopted from the Python Coding YouTube channel Day 24."""

import random
import itertools

# Create a list of all possible card suits and ranks using itertools.products
cards = list(itertools.product(["Diamonds", "Spades", "Hearts", "Clubs",], [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]))

def pick_a_card():
    """A function to pick a random card from the deck """
    if not cards:
        return "No cards left in the deck!"
    card = random.choice(cards)
    cards.remove(card) #Remove selected card from deck to ensure it doesn't repeat
    return f"The {card[1]} of {card[0]}"

print(pick_a_card())

