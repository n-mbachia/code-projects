#!/usr/bin/python3

def read_data():
    """ Read data from a file or database"""
    return[0, 1, 2, 3, 4, 5, 6, 76, 8, 9]

sample = read_data()

def mean(data):
    return sum(data)/ len(data)

average = mean(sample)
