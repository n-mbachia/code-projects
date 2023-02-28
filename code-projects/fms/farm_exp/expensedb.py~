#!/usr/bin/python3

import sqlite3
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import TOP 
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog

def create_table():
    global conn, c
    # Connect to the database
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()

    # Create the expense table
    c.execute('''CREATE TABLE IF NOT EXISTS expense (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT,
                date TEXT,
                amount REAL,
                item TEXT,
                category TEXT,
                enterprise TEXT)''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Create a GUI window
window = tk.Tk()
window.title("Farm Manager Finances")

# Set the window size and position
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (width/2, height))

window.resizable(width, height)
# window.attributes('-alpha', 0.3)
window.attributes('-topmost', 1)
# Create a function for data entry to the database
def dataEntry():
    try:
        # Get the user input from the GUI window
        user_name = e1_val.get()
        date = e2_val.get()
        amount = e3_val.get()
        item = e4_val.get()
        category = e5_val.get()
        enterprise = e6_val.get()

        # Check if all fields are filled            
        if user_name == '' or date == '' or amount == '' or item == '' or category == '' or enterprise == '':
            messagebox.showerror("Error", "Please fill all fields.")
            return

        # Connect to the database
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()

        # Insert the data into the database table
        c.execute("INSERT INTO expense (user_name, date, amount, item, category, enterprise) VALUES (?, ?, ? ,?, ? ,?)",
            (user_name, date, amount, item, category, enterprise))
        conn.commit()
        messagebox.showinfo("Success", "Data added successfully")

        # Clear the input fields
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create labels and entry boxes for user input
l1 = Label(window, text="User Name")
l1.grid(row=0, column=0, sticky='w')
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1, sticky='w')

# Create labels and entry boxes for date input
l2 = Label(window, text="Date (DD/MM/YYYY)")
l2.grid(row=1, column=0, sticky='w')
e2_val = StringVar()
e2 = Entry(window, textvariable=e2_val)
e2.grid(row=1, column=1)

# Create labels and entry boxes for amount input
l3 = Label(window, text="Amount")
l3.grid(row=2, column=0, sticky='w')
e3_val = StringVar()
e3 = Entry(window, textvariable=e3_val)
e3.grid(row=2, column=1)

# Create labels and entry boxes for type input
l4 = Label(window, text="Item Description")
l4.grid(row=3, column=0, sticky='w')
e4_val = StringVar()
e4 = Entry(window, textvariable=e4_val)
e4.grid(row=3, column=1)

# Define categories as a list
categories = ['income', 'Expense', 'Loan']

# Create the label and Combobox for the category
l5 = tk.Label(window, text="Category:")
l5.grid(row=4, column=0, sticky='w')

# Create a StringVar to store the selected category
e5_val = tk.StringVar()

# Create a Combobox with the categories as options
e5 = ttk.Combobox(window, textvariable=e5_val, values=categories)

# Set the default value for the Combobox
e5.current(0)

# Add the Combobox to the window
e5.grid(row=4, column=1, sticky='w')

# Add a button to allow the user to add a new category
add_button = tk.Button(window, text="Add Category", command=lambda: add_category(e5, e5_val))
add_button.grid(row=4, column=2)

def add_category(combobox, stringvar):
    # Get the current value of the Combobox
    current_value = stringvar.get()

    # Get the current list of categories
    current_categories = combobox['values']

    # If the current value is not already in the list of categories, add it        
    if current_value not in current_categories:
        current_categories = list(current_categories) + [current_value]
    combobox['values'] = current_categories

    # Set the selected value to the new value
    combobox.current(current_categories.index(current_value))

# Create labels and entry boxes for enterprise input
l6 = Label(window, text="Enterprise")
l6.grid(row=5, column=0, sticky='w')
e6_val = StringVar()
e6 = Entry(window, textvariable=e6_val)
e6.grid(row=5, column=1)

tree = ttk.Treeview(window)
tree['columns'] = ('ID', 'User Name', 'Date', 'Amount', 'Item Description', 'Category', 'Enterprise')

def create_widgets():
    global tree, search_entry, search_button
    
    # Create a Treeview widget
    tree.heading("#0", text="", anchor="w")
    tree.heading("ID", text="ID", anchor="w")
    tree.heading("User Name", text="User Name", anchor="w")
    tree.heading("Date", text="Date", anchor="w")
    tree.heading("Amount", text="Amount", anchor="w")
    tree.heading("Item Description", text="Expense Type", anchor="w")
    tree.heading("Category", text="Category", anchor="w")
    tree.heading("Enterprise", text="Enterprise", anchor="w")
    tree.column("#0", width=0, stretch="no")
    tree.column("ID", width=50, anchor="w")
    tree.column("User Name", width=100, anchor="w")
    tree.column("Date", width=100, anchor="w")
    tree.column("Amount", width=100, anchor="w")
    tree.column("Item Description", width=100, anchor="w")
    tree.column("Category", width=100, anchor="w")
    tree.column("Enterprise", width=100, anchor="w")
    
    # Add scrollbar to the treeview
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.grid(row=8, column=1, sticky='ns')
    tree.configure(yscrollcommand=vsb.set)

# Add the tree widget to the window
tree.grid(row=8, column=0, sticky='nsew')
window.grid_rowconfigure(0, weight=0)
window.grid_columnconfigure(0, weight=0)

# Call the create_widgets() function
create_widgets()
"""
def search():
    global tree, search_entry
        
    # Get the search keyword from the search entry widget
    keyword = search_entry.get()
    # Convert the keyword to lowercase
    keyword = keyword.lower()

    # Connect to the database
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()

    # Execute the SQL query with the search keyword
    c.execute("SELECT * FROM expense WHERE LOWER('User Name') LIKE ? OR LOWER('Item Description') LIKE ? OR LOWER('Category') LIKE ? OR LOWER('Enterprise') LIKE ?",
        ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))

    # Fetch the results from database
    records = c.fetchall()

    # Clear the existing data from the treeview
    for row in tree.get_children():
        tree.delete(row)

    # If there are no records, display a message in the treeview
    if not records:
        tree.insert('', 'end', values=("No matching records found", "", "", "", "", "", ""))

    # Insert the new data into the treeview
    for row in records:
        tree.insert('', 'end', values=row)
                
# Create a search entry widget
search_entry = Entry(window)
search_entry.grid(row=6, column=0, sticky='w')
        
# Create a search button
search_button = Button(window, text="Search", width=12, command=search)
search_button.grid(row=6, columnspan=2)
"""
     
# Define the show_data function
def show_data():
    # Connect to the database
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()

    # Execute the SQL query
    c.execute("SELECT * FROM expense ORDER BY id DESC")

    # Fetch the results from database
    records = c.fetchall()

    # Clear the existing data from the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert the new data into the treeview
    for row in records:
        tree.insert('', 'end', values=row)

    # Schedule the function to run again after 5 seconds
    window.after(5000, show_data)

# Get data from the SQL database
show_data()
    
# Refresh the treeview with updated data
def search_data():
    # Connect to the database                                                                          
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()

    # Execute a SELECT statement to retrieve the data                                                     
    c.execute("SELECT * FROM expense")

    # Clear the treeview of any existing data                                                           
    tree.delete(*tree.get_children())

    # Insert the retrieved data into the treeview                                                       
    for row in c.fetchall():
        tree.insert("", "end", values=row)

    # Disconnect from the database                                                                      
    conn.close()
    search_data()

def editData():
    # Get the selected item from the treeview widget                                                   
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an item to edit.")
        return
    item_id = selected_item[0]

    # Get the user inputs from the GUI window                                                          
    user_name = e1_val.get()
    date = e2_val.get()
    amount = e3_val.get()
    type = e4_val.get()
    category = e5_val.get()
    enterprise = e6_val.get()

    # Connect to the database                                                                          
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()

    # Update the data in the database table                                                            
    c.execute("UPDATE expense SET user_name=?, date=?, amount=?, item=?, category=?, enterprise=? WHERE id=?", (user_name, date, amount, type, category, enterprise, item_id))
    conn.commit()
    messagebox.showinfo("Success", "Data edited successfully")

    # Clear the input fields                                                                           
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
                                                            
# Create a button to edit the stored database
b2 = Button(window, text="Edit", width=12, command=editData) 
b2.grid(row=7, columnspan=2)
# Define a function to update the database with the edited item
def update_data():
    # Get the edited data from the entry boxes
    user_name = e1_val.get()
    date = e2_val.get()
    amount = e3_val.get()
    type = e4_val.get()
    category = e5_val.get()
    enterprise = e6_val.get()

    # Update the data in the database table
    try:
        c.execute("UPDATE expense SET user_name=?, date=?, amount=?, item=?, category=?, enterprise=? WHERE id=?", (user_name, date, amount, type, category, enterprise, item_id))
        conn.commit()
        messagebox.showinfo("Success", "Data edited successfully")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", f"Unable to update data: {str(e)}")
    # Create a button to add data to the database
b1 = Button(window, text="Enter", width=12, command=dataEntry)
b1.grid(row=6, columnspan=2)

# Start the main event loop
window.mainloop()
