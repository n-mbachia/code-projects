#!/usr/bin/python3
"""This is adopted from Python Coding YouTube channel Day 12"""

# pip3 install langdetect 
from langdetect import detect, LangDetectException

"""This block allows exception if input text is too short or co0mntains non-text characters. 
"""

try:
    text = input("Enter any text in any language: ")
    detected_language = detect(text)
    print(f"The detected language is {detected_language}")
except LangDetectException:
    print("Error: Could not detect the language")

# successful execution will give initial of language;
# input 'hakuna matata'
# output 'sw' meaning Swahili
