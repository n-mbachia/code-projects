#!/usrs/bin/python3
"""This code was adopted from Python Coding Youtube channel day 57..."""

from PyPDF2 import PdfWriter, PdfReader
import getpass

pdfwriter=PdfWriter()
pdf = PdfReader("/Users/mbachia/code-projects/learning/python-365/36 Questions.pdf")
for page_number in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_number])
password=getpass.getpass(prompt="Enter a password: ")
pdfwriter.encrypt(password)
with open("/Users/mbachia/code-projects/learning/python-365/36 Questions.pdf", "wb") as f:
    """The secondary parameter 'wb' is passed on to ensure file is opened in binary mode in order to write bytes to a file"""
    pdfwriter.write(f)

print("Now file is password protected")

