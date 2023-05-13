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
import numpy as np
import sys
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from tkcalendar import DateEntry

def create_table():
    # Connect to the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Create the finance table if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS finance (
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

# Create a function to add data to the database
def add():
    try:
        # Get the user inputs from the GUI window
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
        conn = sqlite3.connect('finance.db')

        # Create the table if it doesn't exist
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS finance
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_name TEXT NOT NULL,
                      date TEXT NOT NULL,
                      amount REAL NOT NULL,
                      item TEXT NOT NULL,
                      category TEXT NOT NULL,
                      enterprise TEXT NOT NULL)''')

        # Insert the data into the database table
        c.execute("INSERT INTO finance (user_name, date, amount, item, category, enterprise) VALUES (?, ?, ? ,?, ? ,?)",
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

# Create a GUI window
window = tk.Tk()
window.title("Farm Financial Manager")

# Set the window size and position
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (screen_width/2, screen_height))

# Create labels and entry boxes for user input
l1 = Label(window, text="User Name:")
l1.grid(row=0, column=0)
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

# Create labels and entry boxes for date input
l2 = Label(window, text="Date (DD/MM/YYYY):")
l2.grid(row=1, column=0)
e2_val = StringVar()
e2 = Entry(window, textvariable=e2_val)
e2.grid(row=1, column=1)

# Create labels and entry boxes for amount input
l3 = Label(window, text="Amount:")
l3.grid(row=2, column=0)
e3_val = StringVar()
e3 = Entry(window, textvariable=e3_val)
e3.grid(row=2, column=1)

# Create labels and entry boxes for type input
l4 = Label(window, text="Item Description:")
l4.grid(row=3, column=0)
e4_val = StringVar()
e4 = Entry(window, textvariable=e4_val)
e4.grid(row=3, column=1)

# Define categories as a list
categories = ['Income', 'Expense', 'Loan']

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
tree['columns'] = ('ID', 'User Name', 'Date', 'Amount', 'Item Description', 'Category', 'Enterprise')

# View the data on the GUI, Connect to the database
conn = sqlite3.connect('finance.db')

# Retrieve data from the 'finance' table
query = "SELECT * FROM finance"
df_from_db = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Create a Text widget to display the data
txt = tk.Text(window)
txt.grid(row=10, column=1)

# Insert the retrieved data into the Text widget
txt.insert(tk.END, df_from_db.to_string(index=False))

def search():
    global tree, search_entry    
    # Get the search keyword from the search entry widget
    keyword = search_entry.get()
    # Connect to the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    # Execute the SQL query with the search keyword
    c.execute("SELECT * FROM finance WHERE 'User Name' LIKE ? OR 'Item Description' LIKE ? OR 'Category' LIKE ? OR 'Enterprise' LIKE ?",
              ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))

    ## Fetch the results from database
    records = c.fetchall()

    # Clear the existing data from the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert the new data into the treeview
    for row in records:
        tree.insert('', 'end', values=row)

def edit_data():
    global tree

    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an item to edit.")
        return
    item_id = selected_item[0]

    # Get the user inputs from the GUI window
    user_name = e1_val.get()
    date = e2_val.get()
    amount = e3_val.get()
    item = e4_val.get()
    category = e5_val.get()
    enterprise = e6_val.get()

    # Validate the user inputs
    if not all([user_name, date, amount, item, category, enterprise]):
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    # Update the data in the database table
    update_data(item_id, user_name, date, amount, item, category, enterprise)

    # Clear the input fields
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)

    # Refresh the treeview with updated data
    refresh_treeview()


def update_data(item_id, user_name, date, amount, item, category, enterprise):
    # Connect to the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Update the data in the database table
    c.execute("UPDATE finance SET user_name=?, date=?, amount=?, item=?, category=?, enterprise=? WHERE id=?",
              (user_name, date, amount, item, category, enterprise, item_id))
    conn.commit()


def refresh_treeview():
    # Clear the existing items in the treeview
    tree.delete(*tree.get_children())

    # Fetch data from the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM finance")
    rows = c.fetchall()

    # Insert the fetched data into the treeview
    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()

def handle_selection(event):
    # Get the selected item from the treeview widget
    selected_item = tree.selection()

    # Perform actions based on the selected item
    if selected_item:
        # Extract the item ID from the selected item
        item_id = selected_item[0]

        # Retrieve the data associated with the selected item
        item_data = tree.item(item_id)

        # Access the values of the selected item
        user_name, date, amount, item, category, enterprise = item_data['values']

        # Populate the input fields with the selected data
        e1_val.set(user_name)
        e2_val.set(date)
        e3_val.set(amount)
        e4_val.set(item)
        e5_val.set(category)
        e6_val.set(enterprise)

# Bind the selection event to the handle_selection function
tree.bind("<<TreeviewSelect>>", handle_selection)

# Define the calendar widget globally
cal = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2)

# Create a function to print database as per selected dates
def export():
    # Connect to the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Get the selected date range from the date picker widget
    start_date = cal_start.get_date()
    end_date = cal_end.get_date()

    # Execute the SQL query
    c.execute("SELECT * FROM finance WHERE Date BETWEEN ? AND ? ORDER BY id DESC",
              (start_date, end_date))

    # Create a Pandas dataframe with the records
    data = c.fetchall()
    df = pd.DataFrame(data, columns=["ID", "User Name", "Date", "Amount", "Item Description", "Category", "Enterprise"])

    if not df.empty:
        try:
            # Export dataframe to Excel
            export_file = filedialog.asksaveasfilename(defaultextension='.xlsx')
            if export_file:
                # Create a new workbook
                wb = Workbook()
                ws = wb.active

                # Write the DataFrame to the worksheet
                for r in dataframe_to_rows(df, index=False, header=True):
                    ws.append(r)

                # Save the workbook to the Excel file
                wb.save(export_file)
                messagebox.showinfo("Success", "Data exported successfully")
            else:
                messagebox.showinfo("Info", "Export cancelled by user")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during export: {str(e)}")
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

# To handle user select input
def handle_click(event):
    print(cal.get_date())

# Create a label widget for cal_start
start_label = tk.Label(window, text="Start Date:", font=("Arial", 12))
start_label.grid(row=8, column=0)

# Create the DateEntry widget for start date
cal_start = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_start.grid(row=8, column=1)
cal.bind("Start Date", handle_click)

# Create a label widget for cal_end
end_label = tk.Label(window, text="End Date:", font=("Arial", 12))
end_label.grid(row=9, column=0)
cal.bind("End Date", handle_click)

# Create the DateEntry widget for end date
cal_end = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_end.grid(row=9, column=1)

# Create a button to add data to the database
b1 = Button(window, text="Enter", width=12, command=add)
b1.grid(row=6, columnspan=2)
# Create a button to edit the stored database                                                          
b2 = Button(window, text="Edit", width=12, command=handle_selection)
b2.bind(handle_selection)
b2.grid(row=7, columnspan=2)

# Create a button to Print to excel last 15 entries
b3 = Button(window, text="Export Report To Excel", width=25, command=export)
b3.grid(row=11, columnspan=2)

# Start the main event loop
while True:
    # Do something
    window.update()
    if window.winfo_exists():
        break
window.mainloop()