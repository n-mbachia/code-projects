#!/usrs/bin/python3
"""The application checks fruits in an initial list and if the fruit is missing in the list its added to the list."""

fruits = ['banana', 'orange', 'mango', 'lemon']

user_input = input("Write the name of any fruit: ").lower()

if user_input in fruits:
    print('That fruit already exists in the list')
else: 
    fruits.append(user_input)
    print(f"The fruit name has been update on the \n {fruits}")


