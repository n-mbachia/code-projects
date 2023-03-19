#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 26"""

# pip3 install forex_python
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
amount = int(input("Enter the amount of money you have: "))

# Get user input for currency name
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

print(from_currency, " To ", to_currency, amount)

result = c.convert(from_currency, to_currency, amount)
print(f'{amount} {from_currency} is equal to {result} {to_currency}')

