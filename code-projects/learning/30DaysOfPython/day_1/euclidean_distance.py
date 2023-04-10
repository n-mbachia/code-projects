#!/usr/bin/python3
"""Euclidean distance can be obtained by measuring the said disntance of the two points. This is also termed as Pythagorous Disntance as it cab be obtained using coordinates."""
import math
x = (2, 3)
y = (10, 8)
distance =math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print(distance)
