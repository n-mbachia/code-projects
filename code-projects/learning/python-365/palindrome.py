def palindrome(string):
    for i in (",.'?/<>}{{}}'"):
        string = string.replace(i, "")
    palindrome = []
    words = string.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome
string = "dad just allowed mum to go to malayalam"
print(palindrome(string))

