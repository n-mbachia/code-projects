#!/usrs/bin/python3
"""This code was adopted from Python Coding Youtube channel day 57..."""

from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

pdfwriter=PdfWriter()
pdf = pdfFilereader("Users/mbachia/code-projects/learning/python-365/36 Questions.pdf")
for page_num in range(pdf.numPage):
    pdfwriter.addPage(pdf.getPage(page_num))
password=getpass.getpass(prompt="Enter a password: ")
pdfwriter.encrypt(password)
with open("Users/mbachia/code-projects/learning/python-365/36 Questions.pdf") as f:
    pdfwriter.write(f)

print("Now file is passwrod protected")

