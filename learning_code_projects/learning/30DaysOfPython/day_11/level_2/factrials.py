#!/usrs/bin/python3
"""Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
A factorial is the multiplication of between 1 and the number itself. This is useful in finding occurences of possibilities. Note the factorials of 0! = 1.  
"""
def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total = total * i
    print(f"The factorial of the {num} is {total}")

user_input = int(input("Enter any number between 1 and 9:\n"))
factorial(user_input)
