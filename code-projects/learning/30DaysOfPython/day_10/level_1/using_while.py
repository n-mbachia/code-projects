#!/usrs/bin/python3
"""This iterates from 10 to 0"""
print("This was printed using the while loop\n")

i = 10 
while i >= 0:
    print(i)
    i = i - 1
print("\nThis was printed using the for loop\n")

nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in nums:
    if i <= 10:
        print(i)
