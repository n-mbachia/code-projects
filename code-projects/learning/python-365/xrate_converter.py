#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 26"""

# pip3 install forex_python
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
cc = CurrencyCodes()
amount = int(input("Enter the amount of money you have: "))

# Get all currency names
currency_names = cc.get_currency_name()

# Display currency names to user
print("Choose a currency:")
for name in currency_name:
    print(name)

# Get user input for currency name
from_currency_name = input("From currency: ")

# Get code for selected currency
from_currency_code = cc.get_code(from_currency_name.upper())

to_currency_name = input("To currency: ")
to_currency_code = cc.get_code(to_currency_name.upper())

print(from_currency_code, " To ", to_currency_code, amount)

result = c.convert(from_currency_code, to_currency_code, amount)
print(f'{amount} {from_currency_code} is equal to {result} {to_currency_code}')

