import tkinter as tk
import sqlite3
from tkinter import messagebox

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

# INSERT BUTTON
insert_button = tk.Button(root, text="Insert", command=insert_data)
insert_button.grid(row=7, column=0, sticky='W')

# CLEAR BUTTON
clear_button = tk.Button(root, text="Clear", command=clear_data)
clear_button.grid(row=7, column=1)

# INSERT DATA INTO THE EXPENSES TABLE
def insert_data():
    try:
        # VALIDATE INPUT TO MAKE SURE ALL NECESSARY DATA IS ENTERED
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

        # CONNECT TO THE EXPENSES DATABASE
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()

        # INSERT DATA INTO EXPENSES TABLE
        cursor.execute("INSERT INTO expenses (Enterprise, Type, Item, Date, Category, Particular, Amount) VALUES (?,?,?,?,?,?,?)",
                      (enterprise_entry.get(), type_entry.get(), item_entry.get(), date_entry.get(), category_entry.get(), particular_entry.get(), amount_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", f"Successfully inserted new data for {item_entry.get()} into the expenses table")
        conn.close()
        clear_data()
    except sqlite3.Error as e:
        messagebox.showerror("Error", e)

#def clear_data():
