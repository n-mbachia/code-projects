def least_common_multiple(a, b):
    if a > b:
        greater  = a
    elif b > a:
        greater = b
    while (True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm
a = int(input("Enter any number greater than zero: "))
b = int(input("Enter another number greater than zero: "))
print(least_common_multiple(a, b))
