#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

def create_widgets():
    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=("ID", "Name"))
    tree.heading("#0", text="", anchor="w")
    tree.heading("ID", text="ID", anchor="w")
    tree.heading("Name", text="Name", anchor="w")
    tree.column("#0", width=0, stretch="no")
    tree.column("ID", width=50, anchor="w")
    tree.column("Name", width=100, anchor="w")

    # Add scrollbar to the treeview
    vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    # Add the tree widget to the window
    tree.pack(expand=YES, fill=BOTH)

    # Insert some data into the tree
    tree.insert('', 'end', values=(1, "Alice"))
    tree.insert('', 'end', values=(2, "Bob"))
    tree.insert('', 'end', values=(3, "Charlie"))

# Create the main window
root = tk.Tk()

# Create a button to open the treeview window
button = tk.Button(root, text="Open Treeview", command=create_widgets)
button.pack()

# Start the event loop
root.mainloop()
