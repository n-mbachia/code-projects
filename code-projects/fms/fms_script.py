#!/usr/python3

import sqlite3 
import datetime
import calendar
import tkinter as tk 
from tkinter import ttk
from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog 
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from tkcalendar import DateEntry


# Create a function to add data to the database
def add():
    # Get the user inputs from the GUI window
    user_name = e1_val.get()
    date = e2_val.get()
    amount = e3_val.get()
    expense_type = e4_val.get()
    category = e5_val.get()
    enterprise = e6_val.get()

    # Check if all fields are filled
    if user_name == '' or date == '' or amount == '' or expense_type == '' or category == '' or enterprise == '':
        messagebox.showerror("Error", "Please fill all fields.")

    # Connect to the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Insert the data into the database table
    c.execute("INSERT INTO finance (user_name, date, amount, type, category, enterprise) VALUES (?, ?, ? ,?, ? ,?)",
              (user_name, date, amount, expense_type, category, enterprise))
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
l2 = Label(window, text="Date (DD/MM/YYYY)")
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
l4 = Label(window, text="Item Description")
l4.grid(row=3, column=0)
e4_val = StringVar()
e4 = Entry(window, textvariable=e4_val)
e4.grid(row=3, column=1)

# Define categories as a list
categories = ['income', 'Expense', 'Loan']

# Create the label and Combobox for the category
l5 = tk.Label(window, text="Category:")
l5.grid(row=4, column=0)

# Create a StringVar to store the selected category
e5_val = tk.StringVar()

# Create a Combobox with the categories as options
e5 = ttk.Combobox(window, textvariable=e5_val, values=categories)

# Set the default value for the Combobox
e5.current(0)

# Add the Combobox to the window
e5.grid(row=4, column=1)

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
l6.grid(row=5, column=0)
e6_val = StringVar()
e6 = Entry(window, textvariable=e6_val)
e6.grid(row=5, column=1)

tree = ttk.Treeview(window)
tree['columns'] = ('ID', 'User Name', 'Date', 'Amount', 'Expense Type', 'Category', 'Enterprise')

def create_widgets():
    # Create a Treeview widget
    global tree
    
    tree.heading("#0", text="", anchor="w")
    tree.heading("ID", text="ID", anchor="w")
    tree.heading("User Name", text="User Name", anchor="w")
    tree.heading("Date", text="Date", anchor="w")
    tree.heading("Amount", text="Amount", anchor="w")
    tree.heading("Type", text="Expense Type", anchor="w")
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
    global tree
    # Connect to the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Execute the SQL query
    c.execute("SELECT * FROM finance ORDER BY id DESC")

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

# Displays database on the window
def view():
    show_data()

view()

# Create a function to edit data in the database 
def edit_data():
    global tree
    # Get the selected item from the treeview widget
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an item to edit.")
        return
    item_id = selected_item[0]

    # Get the user inputs from the GUI window 
    id = selected_item[0]
    user_name = e1_val.get() 
    date = e2_val.get() 
    amount = e3_val.get() 
    type = e4_val.get() 
    category = e5_val.get() 
    enterprise = e6_val.get() 

    # Connect to the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Update the data in the database table 
    c.execute("UPDATE finance SET user_name=?, date=?, amount=?, expense_type=?, category=?, enterprise=? WHERE id=?", (user_name ,date ,amount ,type ,category ,enterprise, id)) 
    conn.commit() 
    messagebox.showinfo("Success", "Data edited successfully") 
            
    # Clear the input fields
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

    # Refresh the treeview with updated data
    edit_data()

# Define the calendar widget globally
cal = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2)

# Create a function to print last 15 entries from the database
def export():
    # Connect to the database                                                                  
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Get the selected date from the date picker widget
    # selected_date = cal.get_date()

    # Get the selected date range from the date picker widget
    start_date = cal_start.get_date()
    end_date = cal_end.get_date()


    # Execute the SQL query                                                                     
    c.execute("SELECT * FROM finance WHERE Date BETWEEN ? AND ? ORDER BY id DESC",
              (start_date, end_date))

    # Fetch the results from database                                                           
    records = c.fetchall()

    # Create a Pandas dataframe with the records
    df = pd.DataFrame(records, columns=["ID", "User Name", "Date", "Amount", "Expense Type", "Category", "Enterprise"])

    if not df.empty:
        # Export dataframe to Excel
        export_file = filedialog.asksaveasfilename(defaultextension='.xlsx')
        df.to_excel(export_file, index=False)
        messagebox.showinfo("Success", "Data exported successfully")
    else:
        messagebox.showerror("Error", "No records found")

    # Close the cursor and the connection
    c.close()
    conn.close() 

# Create the date picker widget
def export_data():
    # Disable the button to prevent multiple exports
    export_button.config(state='disabled')

    # Call the export function
    export()

    # Re-enable the button after the export is complete
    export_button.config(state='normal')

# Create a label widget for cal_start
start_label = tk.Label(window, text="Start Date:", font=("Arial", 12))
start_label.grid(row=8, column=0)

# To handle user select input
def handle_click(event):
    print(cal.get_date())

# Create the DateEntry widget for start date
cal_start = DateEntry(window, width=12, background='darkblue',
                      foreground='white', borderwidth=2)
cal_start.grid(row=9, column=0)
cal.bind("Start Date", handle_click)

# Create a label widget for cal_end
end_label = tk.Label(window, text="End Date:", font=("Arial", 12))
end_label.grid(row=8, column=1)
cal.bind("End Date", handle_click)

# Create the DateEntry widget for end date
cal_end = DateEntry(window, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
cal_end.grid(row=9, column=1)

# Create a button to add data to the database
b1 = Button(window, text="Enter", width=12, command=add)
b1.grid(row=6, columnspan=2)
# Create a button to edit the stored database
b2 = Button(window, text="Edit", width=12, command=edit_data) 
b2.grid(row=7, columnspan=2)
# Create a button to Print to excel last 15 entries
b3 = Button(window, text="Export Report To Excel", width=25, command=export)
b3.grid(row=10, columnspan=2)
# Create a button to display data in a Treeview widget
# b4= Button(window, text="View data", width=15, command=create_widgets)
# b4.grid(row=9, columnspan=2)

# Start the main event loop
window.mainloop()
