#!/usrs/bin/python3

for i in range(0, 7): # handles number of rows as specified in range function
    for j in range(0, i+1): # handles number of columns
        print("#", end="") # prints hash
    print("\r") # ending line after each row

