#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 30..."""


import getpass # Built-in Python Package
database = {"mncoding": "123", "mbachia": "124545"}
username = input("Enter your Username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your passwprd again: ")
        break
print("Verified")
