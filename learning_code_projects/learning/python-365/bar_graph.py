#!/usr/bin/python3
"""This code was adopted from Python Coding Youtube Channels day 28..."""

import matplotlib.pyplot as pyplot

# Set us the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

# Sort the data
labels, sizes = zip(*sorted(zip(labels, sizes), key=lambda x: x[1]))
"""The 'zip()' function is used to create a tuple list. '*' operator unpacks the list of tuples into seperate arguments.while the 'zip(labels, sizes)' creates a list of tuiples with elements from 'labels' and 'sizes'. When the 'sorted' function is called to the list of tuples, the key paramemter to a lambda function specifies the values be sorted in ascending order using 'sizes' as paramemter."""

# Set up the bar chart
pyplot.bar(index, sizes, tick_label=labels)

# Configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('Programming Languages')
pyplot.title('Programming Languages Usage')

# Add gridlines
pyplot.grid(axis='y')

# Rotate the lables by angle
pyplot.xticks(rotation=45)

# Display the chart
pyplot.show()
