#!/usr/bin/python3

import matplotlib.pyplot as plt
import squarify

labels = ["A", "B", "C", "D","E", "F", "G", "H", "I", "J"]
sizes = [100, 75, 50, 25, 20, 10, 5, 2, 1, 0.5]

fig, ax = plt.subplots()
squarify.plot(sizes=sizes, label=labels, ax=ax)
plt.show()

