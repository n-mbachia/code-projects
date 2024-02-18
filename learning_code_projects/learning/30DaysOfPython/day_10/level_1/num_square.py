#!/usrs/bin/python3
"""A range of numbers to generate squares of those numbers"""

start = 0
end = 10
for i in range(start, end + 1):
    square = i * i
    print(f"{i} X {i} = {square}")
