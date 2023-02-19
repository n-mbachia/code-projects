#!/usr/python3

import sqlite3 
import tkinter as tk 
from tkinter import ttk
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog 
import pandas as pd 

# Connect to the database
conn = sqlite3.connect('finance.db')
c = conn.cursor()

# Create a function to add data to the database
def add():
    # Get the user inputs from the GUI window
    user_name = e1_val.get()
    date = e2_val.get()
    amount = e3_val.get()
    ftype = e4_val.get()
    category = e5_val.get()
    enterprise = e6_val.get()

    # Insert the data into the database table
    c.execute("INSERT INTO finance (user_name, date, amount, type, category, enterprise) VALUES (?, ?, ? ,?, ? ,?)",
              (user_name, date, amount, ftype, category, enterprise))
    conn.commit()
    messagebox.showinfo("Success", "Data added successfully")

    # Clear the input fields
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

# Create a GUI window
window = tk.Tk()
window.title("Farm Manager Finances")

# Set the window size and position
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (width/2, height))


# Create labels and entry boxes for user input
l1 = Label(window, text="User Name")
l1.grid(row=0, column=0)
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

# Create labels and entry boxes for date input
l2 = Label(window, text="Date")
l2.grid(row=1, column=0)
e2_val = StringVar()
e2 = Entry(window, textvariable=e2_val)
e2.grid(row=1, column=1)

# Create labels and entry boxes for amount input
l3 = Label(window, text="Amount")
l3.grid(row=2, column=0)
e3_val = StringVar()
e3 = Entry(window, textvariable=e3_val)
e3.grid(row=2, column=1)

# Create labels and entry boxes for type input
l4 = Label(window, text="Type")
l4.grid(row=3, column=0)
e4_val = StringVar()
e4 = Entry(window, textvariable=e4_val)
e4.grid(row=3, column=1)

# Create labels and entry boxes for category input
l5 = Label(window, text="Category")
l5.grid(row=4, column=0)
e5_val = StringVar()
e5 = Entry(window, textvariable=e5_val)
e5.grid(row=4, column=1)

# Create labels and entry boxes for enterprise input
l6 = Label(window, text="Enterprise")
l6.grid(row=5, column=0)
e6_val = StringVar()
e6 = Entry(window, textvariable=e6_val)
e6.grid(row=5, column=1)

def create_widgets():
    # Create a Treeview widget
    global tree
    tree = ttk.Treeview(window, columns=("ID", "User Name", "Date", "Amount", "Type", "Category", "Enterprise"))
    tree.heading("#0", text="", anchor="w")
    tree.heading("ID", text="ID", anchor="w")
    tree.heading("User Name", text="User Name", anchor="w")
    tree.heading("Date", text="Date", anchor="w")
    tree.heading("Amount", text="Amount", anchor="w")
    tree.heading("Type", text="Type", anchor="w")
    tree.heading("Category", text="Category", anchor="w")
    tree.heading("Enterprise", text="Enterprise", anchor="w")
    tree.column("#0", width=0, stretch="no")
    tree.column("ID", width=50, anchor="w")
    tree.column("User Name", width=100, anchor="w")
    tree.column("Date", width=100, anchor="w")
    tree.column("Amount", width=100, anchor="w")
    tree.column("Type", width=100, anchor="w")
    tree.column("Category", width=100, anchor="w")
    tree.column("Enterprise", width=100, anchor="w")
    # tree.grid(row=7, column=0, columnspan=2)
    
    # Add scrollbar to the treeview
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    # Add the tree widget to the window
    tree.pack(expand=YES, fill=BOTH)

    
    # Get data from the SQL database
    def show_data():
        c.execute("SELECT * FROM finance ORDER BY id DESC LIMIT 15")
        records = c.fetchall()
        for row in tree.get_children():
            tree.delete(row)
        for row in records:
            tree.insert('', 'end', values=row)

        # Display the data in the Treeview widget
        def view():
            show_data(tree)

        # Call the view() function to display the data when the program starts
        view()

# Create a function to edit data in the database 
def edit(): 
    # Get the user inputs from the GUI window 
    id = c.lastrowid
    user_name = e1_val.get() 
    date = e2_val.get() 
    amount = e3_val.get() 
    type = e4_val.get() 
    category = e5_val.get() 
    enterprise = e6_val.get() 

    # Update the data in the database table 
    c.execute("UPDATE finance SET user_name=?, date=?, amount=?, type=?, category=?, enterprise=? WHERE id=?", (user_name ,date ,amount ,type ,category ,enterprise, id)) 
    conn.commit() 
    messagebox.showinfo("Success", "Data edited successfully") 

# Create a function to print last 15 entries from the database 
def export(): 
    c.execute("SELECT * FROM finance ORDER BY id DESC LIMIT 15")
    records = c.fetchall()
    if len(records) > 0:
        df = pd.DataFrame(records)
        df.columns = ["ID", "User Name", "Date", "Amount", "Type", "Category", "Enterprise"]
        export_file= filedialog.asksaveasfilename(defaultextension='xlsx')
        df.to_excel(export_file + ".xlsx",index = False)
        messagebox.showinfo("Sucess", "Data exported successfully")
    else:
        messagebox.showerror("Error", "No records found")

# Create a button to add data to the database
b1 = Button(window, text="Enter", width=12, command=add)
b1.grid(row=6, columnspan=2)
b2 = Button(window, text="Edit", width=12, command=edit) 
b2.grid(row=7, columnspan=2)
b3 = Button(window, text="Print Last 15 Entries", width=25, command=export)
b3.grid(row=8, columnspan=2)
# Create a button to display data in a Treeview widget
b4= Button(window, text="View data", width=15, command=create_widgets)
b4.grid(row=9, columnspan=2)


# Start the main event loop
window.mainloop()

