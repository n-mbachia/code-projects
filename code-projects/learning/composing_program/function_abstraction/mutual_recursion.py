#!/usr/bin/python3

def is_even(n):
    if n == 0:
        return True
    else:
        if (n-1) == 0:
            return False
        else:
            return is_even((n-1)-1)

n = int(input("Enter any whole number: "))
result = is_even(n)

print(f"{n} is even: {result}")
