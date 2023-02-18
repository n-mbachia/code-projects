import textwrap
text = """ 'textwrap' is a built-in Python module. This code snippet, formatS the variable text using the 'fill()' method of the 'TextWrapper' object to wrap text and returning a single string with wrapped lines the width. Useful applications include: text justification, preparing text for analysis. preparing text for display on user interface, when writing text to file and adjusting text to console window"""

wrapper = textwrap.TextWrapper(width=55)

wrapped_text = wrapper.fill(text)

print(wrapped_text)
