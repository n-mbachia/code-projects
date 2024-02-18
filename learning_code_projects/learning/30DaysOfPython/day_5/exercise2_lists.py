#!/usr/bin/python3

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list of age
ages.sort()
print(ages,'\n')

# Find the minimum and maximum ages
min_age = ages[0]
max_age = ages[-1]

print("Minimum age:", min_age,'\n')
print("Maximum age:", max_age,'\n')
print("The total number of ages is:", len(ages),'\n')
