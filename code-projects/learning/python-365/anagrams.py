#!/usr/bin/python3

"""The code was adopted from Python Coding YouTube channel Day 24"""

def anagram(word1, word2):
    """Checks if two words are anagrams. 
    arguments are word1 a string and word2 a string
    Returns a bool if the two words are anagrams, False otherwise"""
    # convert words to lowercase
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2) # sorts each words letters and compares them

print(anagram("cinema", "iceman"))
print(anagram("men", "women"))
print(anagram("cool", "loco"))
print(anagram("a gentleman", "elegant man"))
print(anagram("William' Shakespeare", "I'll make a wise phrase"))
