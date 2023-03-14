#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube Channel Day 25"""

import PyPDF2

filename = input("Enter the file name of a PDF file: ")
search_term = input("Enter the seatch term: ")

with open(filename, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)

    for page in range(num_pages):
        current_page = reader.pages[page]
        text = current_page.extract_text()
        if search_term in text:
            print(f"Page {page+1}:")
            print(text)
