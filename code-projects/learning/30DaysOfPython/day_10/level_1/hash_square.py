#!/usrs/bin/python3
num_rows = 8
num_cols = 8

for i in range(num_rows): # loops through rows
    for j in range(num_cols): # loops through columns
        print("# ", end="" ) # prints chracter followed by space without a newline
    print("\r") # moves to next row

