#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 29..."""

def format_ip_address(address):
    return address.replace(".", "[.]")

ip_address = input("Enter your IP address: ")
formatted_address = format_ip_address(ip_address)
print(f"Formated IP address: {formatted_address}")
