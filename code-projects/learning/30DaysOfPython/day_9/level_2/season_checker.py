#!/usrs/bin/python3

"""Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer"""

user_input = input("Enter any month to check the season it falls in:").lower()

if user_input in ['september', 'october', 'november']:
    print("Autumn")
elif user_input in ['december', 'january', 'february']:
    print("Winter")
elif user_input in ['march', 'april', 'may']:
    print("Spring")
elif user_input in ['june', 'july', 'august']:
    print("Summer")
else:
    print("invalid input. please eneter a valid month")
