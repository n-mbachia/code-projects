import tkinter as tk
import sqlite3
from tkinter import messagebox


def create_table():
    # connect to the database
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    # create the expenses table
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (Enterprise TEXT NOT NULL, Type TEXT NOT NULL, Item TEXT NOT NULL, Date DATE NOT NULL, Category TEXT NOT NULL, Particular TEXT NOT NULL, Amount REAL NOT NULL)''')
    conn.commit()
    conn.close()


def insert_data():
    try:
        # validate input
        if not enterprise_entry.get():
            messagebox.showerror("Error", "Enterprise field is empty")
            return
        if not type_entry.get():
            messagebox.showerror("Error", "Type field is empty")
            return
        if not item_entry.get():
            messagebox.showerror("Error", "Item field is empty")
            return
        if not date_entry.get():
            messagebox.showerror("Error", "Date field is empty")
            return
        if not category_entry.get():
            messagebox.showerror("Error", "Category field is empty")
            return
        if not particular_entry.get():
            messagebox.showerror("Error", "Particular field is empty")
            return
        if not amount_entry.get() or not amount_entry.get().isnumeric():
            messagebox.showerror("Error", "Invalid amount")
            return

        # connect to the database
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (Enterprise, Type, Item, Date, Category, Particular, Amount) VALUES (?,?,?,?,?,?,?)",
                       (enterprise_entry.get(), type_entry.get(), item_entry.get(), date_entry.get(), category_entry.get(), particular_entry.get(), amount_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", f"Successfully inserted new data for {item_entry.get()} into the expenses table")
        conn.close()
        clear_data()
    except sqlite3.Error as e:
        messagebox.showerror("Error", e)


def clear_data():
    enterprise_entry.delete(0, END)
    type_entry.delete(0, END)
    item_entry.delete(0, END)
    date_entry.delete(0, END)
    category_entry.delete(0, END)
    particular_entry.delete(0, END)
    amount_entry.delete(0, END)


# CREATING A GUI WINDOW
root = tk.Tk()
root.title("Expenses Data Entry")

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


def display_data():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    # FETCH ALL DATA FROM THE EXPENSES TABLE
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    # CLEAR THE TABLE BEFORE POPULATING IT WITH NEW DATA
    for i in table.get_children():
        table.delete(i)
    # POPULATE THE TABLE WITH THE FETCHED DATA
    for row in data:
        table.insert("", END, values=row)
    conn.close()


def search_data():
    # CONNECT TO THE DATABASE
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    # FETCH DATA FROM THE EXPENSES TABLE WHERE THE ITEM MATCHES THE SEARCH TERM
    cursor.execute("SELECT * FROM expenses WHERE Item=?", (search_var.get(),))
    data = cursor.fetchall()
    # CLEAR THE TABLE BEFORE POPULATING IT WITH NEW DATA
    for i in table.get_children():
        table.delete(i)
    # POPULATE THE TABLE WITH THE FETCHED DATA
    for row in data:
        table.insert("", END, values=row)
    conn.close()


def update_data():
    # CONNECT TO THE DATABASE
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    # UPDATE THE SELECTED ROW IN THE EXPENSES TABLE
    cursor.execute("UPDATE expenses SET Enterprise=?, Type=?, Item=?, Date=?, Category=?, Particular=?, Amount=? WHERE id=?", (enterprise_entry.get(), type_entry.get(), item_entry.get(), date_entry.get(), category_entry.get(), particular_entry.get(), amount_entry.get(), selected_item[0]))
    conn.commit()
    messagebox.showinfo("Success", f"Successfully updated data for {item_entry.get()} in the expenses table")
    conn.close()
    clear_data()
    display_data()


def delete_data():
    # CONNECT TO THE DATABASE
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    # DELETE THE SELECTED ROW FROM THE EXPENSES TABLE
    cursor.execute("DELETE FROM expenses WHERE id=?", (selected_item[0],))
    conn.commit()
    messagebox.showinfo("Success", f"Successfully deleted data for {item_entry.get()} from the expenses table")
    conn.close()
    clear_data()
    display_data()

create_table()
    # CREATE THE TABLE
    table = ttk.Treeview(root, columns=("Enterprise", "Type", "Item", "Date", "Category", "Particular", "Amount"))
    table.heading("#0", text="ID")
    table.heading("Enterprise", text="Enterprise")
    table.heading("Type", text="Type")
    table.heading("Item", text="Item")
    table.heading("Date", text="Date")
    table.heading("Category", text="Category")
    table.heading("Particular", text="Particular")
    table.heading("Amount", text="Amount")
    table.column("#0", stretch=tk.NO, minwidth=0, width=0)
    table.column("Enterprise", stretch=tk.NO, minwidth=0, width=150)
    table.column("Type", stretch=tk.NO, minwidth=0, width=150)
    table.column("Item", stretch=tk.NO, minwidth=0, width=150)
    table.column("Date", stretch=tk.NO, minwidth=0, width=150)
    table.column("Category", stretch=tk.NO, minwidth=0, width=150)
    table.column("Particular", stretch=tk.NO, minwidth=0, width=150)
    table.column("Amount", stretch=tk.NO, minwidth=0, width=150)
    table.grid(row=10, column=0, columnspan=7, padx=20, pady=20, ipadx=100)
    # BIND THE SELECTED ROW TO A VARIABLE
    table.bind("<ButtonRelease-1>", selected_item)
    display_data()

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
submit_button = tk.Button(root, text="Submit", command=insert_data)
clear_button = tk.Button(root, text="Clear", command=clear_data)

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

