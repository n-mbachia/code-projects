#!/usr/bin/python3
"""Euclidean distance in mathematics is distance or Euclidean metric os the "ordinary" (straight line) between two spaces in Euclidean space. Also termed as Pythagorous Disntance as it cab be obtained using coordinates."""
import math

x = (2, 3)
y = (10, 8)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print(f"Eulidean distance from x to y:",distance)
