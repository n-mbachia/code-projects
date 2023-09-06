#!/usrs/bin/python3
"""Use for loop to iterate through 0 - 100 and find the sum of add and even numbers."""

sum_even = 0
sum_odd = 0 

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f'The sum of all even is',sum_even,'.','And the sum of all odds is', sum_odd)
