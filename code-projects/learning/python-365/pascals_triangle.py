#!/usr/bin/python3
"""This code was adopted from the Python Coding Channel on Youtube Day 33..."""

def print_pascal(n):
    """function that takes n as its input"""
    arr = [1] # initialize the array with the first row
    temp = [] # create an empty array to hold the next row
    print("Pascal's triangle of", n, "Rows....")
    for i in range(n):
        # print the row number and the elements in the row
        print("row", i+1, end=": ")
        for j in range(len(arr)):
            print(arr[j], end=" ")
        print()
        # calculate the next row using the current row
        temp.append(1) # the first element is always 1
        for j in range(len(arr)-1):
            temp.append(arr[j] + arr[j + 1]) # calculate the value of the next element
        temp.append(1) # the last element is always 1
        arr = temp # set the current row to the next row
        temp = [] # clear the temp array for the next row

# get the number of rows from the user
n = int(input("Enter the number of rows in Pascal's triangle: "))
print_pascal(n)

