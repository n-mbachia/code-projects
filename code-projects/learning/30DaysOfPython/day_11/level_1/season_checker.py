#!/usr/bin/python3
"""Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer."""

def check_season():
    """Checks season of the year
    
    Arguments:
     User input provided as argument

    Returns:
     Autumn, Winter, Sprint, Summer"""

    user_input = input('Enter any month: ').lower()
    if user_input in ['september', 'october', 'november']:
        print('Autumn')
    elif user_input in ['december', 'january', 'february']:
        print('Winter')
    elif user_input in ['march', 'april', 'may']:
        print('Spring')
    else:
        print('Summer')
check_season()
