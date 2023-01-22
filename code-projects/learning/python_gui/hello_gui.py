#IMPORT DISPLAY SCREEN WINDOW
import tkinter as tk


# CREATES CLASS INSTANCE FOR PYTHON 2 AND 3
root = tk.Tk()

# PLACE WIDGET BELOW ROOT WINDOW
message = tk.Label(root, text="""Hello, n-mbachia, You are learning about tkinter, a widget syntax has a container (window or frame) and options and a keyword argument""")

#IF NOT CALLED WIDGET IS INVINSIBLE
message.pack()


# TO ENSURE WE RUN ON ALL PLATFORMS FUNCTION USED BELOW
try:
	from ctypes import windll

	windll.shcore.SetProcessDpiAwareness(1)
finally:
	# CALLS MAIN LOOP KEEPING WINDOW OPEN PLACED AS LAST STATEMENT IN PROGRAM
	root.mainloop()
