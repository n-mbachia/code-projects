#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel day 48... """

def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_number = lst[i]
        for j in range(i - 1, -1, -1):
            if lst[j] > current_number:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else:
                lst[j + 1] = current_number
                break
    return lst

if __name__ == '__main__':
    # integers
    lst = [5, 8, 4, 2, 6, 3, 1, 9, 7, 0]
    print(f"List to be sorted is :{lst}","\nWhile sorted list is:", insertion_sort(lst),'\n')
    # alphabets
    lst = ['q', 'w', 'm', 'M', 'B', 'C' 'd', 'Z', 'z', 'a', 'A']
    print(f"List to be sorted is :{lst}","\nWhile sorted list is:", insertion_sort(lst), '\n')
    lst = ['zip', 'SKY', 'Cartoon', 'sky', 'George W. Bush', 'George w. Bush', 'cartoon', 'Zip', 'Sky']
    print(f"List to be sorted is :{lst}","\nWhile sorted list is:", insertion_sort(lst), '\n')
