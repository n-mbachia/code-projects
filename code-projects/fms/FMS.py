import tkinter as tk
import sqlite3
from tkinter import messagebox


root = tk.Tk()
root.title("Expenses Data Entry")

# Create the labels
enterprise_label = tk.Label(root, text="Enterprise:")
type_label = tk.Label(root, text="Type:")
item_label = tk.Label(root, text="Item:")
date_label = tk.Label(root, text="Date:")
category_label = tk.Label(root, text="Category:")
particular_label = tk.Label(root, text="Particular:")
amount_label = tk.Label(root, text="Amount:")

# Create the Entry widgets
enterprise_entry = tk.Entry(root)
type_entry = tk.Entry(root)
item_entry = tk.Entry(root)
date_entry = tk.Entry(root)
category_entry = tk.Entry(root)
particular_entry = tk.Entry(root)
amount_entry = tk.Entry(root)

# Create the button
submit_button = tk.Button(root, text="Submit", command="insert_data")
clear_button = tk.Button(root, text="Clear", command="clear_data")

# Create the table
table = tk.ttk.Treeview(root, columns=("Enterprise","Type","Item","Date","Category","Particular","Amount"))
table.heading("#0", text="Enterprise")
table.heading("#1", text="Type")
table.heading("#2", text="Item")
table.heading("#3", text="Date")
table.heading("#4", text="Category")
table.heading("#5", text="Particular")
table.heading("#6", text="Amount")

# Layout the widgets using grid layout
enterprise_label.grid(row=0, column=0, sticky="W")
enterprise_entry.grid(row=0, column=1)
type_label.grid(row=1, column=0, sticky="W")
type_entry.grid(row=1, column=1)
item_label.grid(row=2, column=0, sticky="W")
item_entry.grid(row=2, column=1)
date_label.grid(row=3, column=0, sticky="W")
date_entry.grid(row=3, column=1)
category_label.grid(row=4, column=0, sticky="W")
category_entry.grid(row=4, column=1)
particular_label.grid(row=5, column=0, sticky="W")
particular_entry.grid(row=5, column=1)
amount_label.grid(row=6, column=0, sticky="W")
amount_entry.grid(row=6, column=1)
submit_button.grid(row=7, column=0, sticky="W")
clear_button.grid(row=7, column=1, sticky="W")
table.grid(row=8, column=0, columnspan=2)

root.mainloop()

