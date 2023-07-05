#!/usr/bin/python3
"""This code was adopted from Python Coding youtube Channel day 71..."""

import imageio
filenames = ["sketch.png", "original.png"]
image = []
for filename in filenames:
    image.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images, "GIF", duration=1)
