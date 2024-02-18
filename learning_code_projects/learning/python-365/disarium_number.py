#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel day 76..."""

Number = int(input("Enter the number to check disarium number = "))
length = len(str(Number))
temp = Number
Sum = 0
rem = 0

while temp > 0:
    rem = temp % 10
    Sum = Sum + int(rem**length)
    temp = temp // 10
    length = length -1

print("the sum of Digits = %d" %Sum)

if Sum == Number:
    print("\n%d is a Disarium Number." %Number)
else: 
    print("\n%d is Not a Disarium Number." %Number)
