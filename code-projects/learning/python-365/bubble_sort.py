#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel day 47..."""

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j -1] = lst[j -1], lst[j]
    return lst

if __name__ == "__main__":
    # float
    lst = [12, 6.9, 3.14, 289.09, 9.3, 12.4]
    print('Sorted List:', bubble_sort(lst))
    # alphabets
    lst = ['q', 'w', 'm', 'M', 'B', 'C' 'd', 'Z', 'z', 'a', 'A']
    print('Sorted List:', bubble_sort(lst))
    lst = ['zip', 'SKY', 'Cartoon', 'sky', 'George W. Bush', 'George w. Bush', 'cartoon', 'Zip', 'Sky']
    print('Sorted List:', bubble_sort(lst))

