#!/usr/bin/python3
"""As another example of mutual recursion, consider a two-player game in which there are n initial pebbles on a table. The players take turns, removing either one or two pebbles from the table, and the player who removes the final pebble wins. Suppose that Alice and Bob play this game, each using a simple strategy:

Alice always removes a single pebble
Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
Given n initial pebbles and Alice starting, who wins the game?

A natural decomposition of this problem is to encapsulate each strategy in its own function. This allows us to modify one strategy without affecting the other, maintaining the abstraction barrier between the two. In order to incorporate the turn-by-turn nature of the game, these two functions call each other at the end of each turn."""

def play_alice(n):
    if n == 0:
        return "Bob wins!"  # return the result
    else:
        return play_bob(n - 1)  # call play_bob function

def is_even(n):
    return n % 2 == 0

def play_bob(n):
    if n == 0:
        return "Alice wins"  # return the result
    elif is_even(n):
        return play_alice(n - 2)  # call play_alice function
    else:
        return play_alice(n - 1)  # call play_alice function

n = int(input("Enter any whole number: "))
result = play_alice(n)

print(f"For {n} the winner is {result}")


"""In play_bob, we see that multiple recursive calls may appear in the body of a function. However, in this example, each call to play_bob calls play_alice at most once. In the next section, we consider what happens when a single function call makes multiple direct recursive calls."""
