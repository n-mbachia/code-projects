x#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube Channel Day 17"""

def age_calculator():
    """ Calculates age as per user entered data.""" 
    import datetime
    while True:
        try:
            dob_str = input("Please enter your date of birth in YYYY-MM-DD format: ")
            dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format. Please enter your date of birth in YYYY-MM-DD format.")
                       
    # Prompts user input to calculates years 
    today = datetime.datetime.now().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    # Print the age in years
    print("Your age is {} years.".format(age))

age_calculator()
