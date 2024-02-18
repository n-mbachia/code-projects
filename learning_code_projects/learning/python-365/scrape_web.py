#!/usr/bin/python3
"""This code was adopted from Python Coding Youtube Channel day 38..."""

import urllib.request
import pandas as pd # pip3 install lxml
from tabulate import tabulate

url = input("Enter a Url: ")

try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
    data = pd.read_html(html)[0]
    print(data.head())
except:
    print("Invalid URLor unable to parse data as HTML.")


