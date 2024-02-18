# CHARACTER OCCURRENCES COUNT
# Define a function
def count_characters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
#  characters to be counted
word = ("""count character \
 occurences using Python""")
# a function call with argument
print(count_characters(word))
