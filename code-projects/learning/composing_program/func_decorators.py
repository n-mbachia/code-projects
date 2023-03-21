#!/usr/bin/python3
"""A decorator in Python is a design pattern that allows modifying the behavior of a function or class without modifying its source code. Decorators wrap a function and modify its behavior in one way or another. They are a powerful feature of Python and are widely used in many Python libraries and frameworks.

In Python, a decorator is implemented as a function that takes another function as an argument and returns a new function that adds some additional behavior to the original function. The new function is typically a wrapper around the original function."""

def my_decorator(func):
    """Function defined that takes a function as argument and returns a new function wrapped"""
    def wrapped():
        """Function outouts the messages before and after calling of argument function"""
        print("func before calling")
        func() # This calls the function after @my_decorator
        print("func After calling")
    return wrapped

@my_decorator # Calling this modifies the behaviour of func defined below.
def say_hello():
    """Function that prints Hello for the user"""
    print("Hello")

say_hello() # Function call
