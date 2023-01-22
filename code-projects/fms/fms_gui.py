#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

from tkinter import messagebox

# CREATING A GUI WINDOW WITH SPECS IN PIXELS
root = tk.Tk()
root.title("Farm Manager")

# WINDOW DIMENSIONS 
window_width = 600
window_height = 600

# GET USER SCREEN DIMENSION
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#FIND THE CENTER POINT
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# SET POSITION TO SCREEN CENTER
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# DECLARE INPUT FIELDS
enterprise_label = tk.Label(root, text="Enterprise:")
enterprise_label.grid(row=0, column=0, sticky='W')
enterprise_entry = tk.Entry(root)
enterprise_entry.grid(row=0, column=1)

type_label = tk.Label(root, text="Type:")
type_label.grid(row=1, column=0, sticky='W')
type_entry = tk.Entry(root)
type_entry.grid(row=1, column=1)

item_label = tk.Label(root, text="Item:")
item_label.grid(row=2, column=0, sticky='W')
item_entry = tk.Entry(root)
item_entry.grid(row=2, column=1)

date_label = tk.Label(root, text="Date:")
date_label.grid(row=3, column=0, sticky='W')
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=4, column=0, sticky='W')
category_entry = tk.Entry(root)
category_entry.grid(row=4, column=1)

particular_label = tk.Label(root, text="Particular:")
particular_label.grid(row=5, column=0, sticky='W')
particular_entry = tk.Entry(root)
particular_entry.grid(row=5, column=1)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=6, column=0, sticky='W')
amount_entry = tk.Entry(root)
amount_entry.grid(row=6, column=1)

# ALLOWS APPLICATION TOI RUN ACROSS PLATFORMS
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
	root.mainloop()


