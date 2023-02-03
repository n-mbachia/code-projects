# LINE CONTINUATION CHARACTER
# The backslash('\') is a line continuation character
# It is used in all versions of python 

print("I'm taking time to try this \
365 Days Python Challenge by #clcoding.com")

# Where would this be applicable?
# Continuation of a long statement
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)
# Line continuation in a multi-line string
quote = """ A language isn't something \
you learn so much as something you join. \
 - Arika Okrent"""

print(quote)

# line continuation in a tuple
t = (1, 2, 3,
     4, 5, 6)

print(t)

# The output remains as intended
