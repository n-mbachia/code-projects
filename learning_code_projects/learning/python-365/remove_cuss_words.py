#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel Day 36..."""

from better_profanity import profanity # pip3 install better_profanity
text = input("Enter your sentence to check: ")
censored = profanity.censor(text)
print(censored)
