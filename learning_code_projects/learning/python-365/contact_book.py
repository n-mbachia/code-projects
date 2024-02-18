#!/usr/bin/python3

"""This code was adopted from Python Coding YouTube channel, Day 22."""

# Initialize empty lists to store contact information.
names = []
phone_numbers = []

# Ask the user how many contacts they want to save and get input.
num = int(input("Enter contact number to save: "))

# Loop through the range of the number of contacts to get name and phone number information.
for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone number: ")
    names.append(name)
    phone_numbers.append(phone_number)

# Print out the table of contacts.
print("\nName\t\t\tPhone Number\n")
for i in range(num):
    print("{}\t\t\t{}", format(names[i], phone_numbers[i]))

# Ask user for a search term
search_term = input("\nEnter search term: ")

#Search for the term in the list of names and print the contact information found.
print("Search results: ")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}", format(search_term, phone_number))
else:
    print("Name not found.")
