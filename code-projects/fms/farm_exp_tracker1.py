#!usr/bin/python3

import sqlite3

conn = sqlite3.connect('expenses.db')

# CREATES A TABLE NAMED "EXPENSES"

conn.execute('''CREATE TABLE expenses
                 (Enterprise TEXT NOT NULL,
                 Type TEXT NOT NULL,
                 Item TEXT NOT NULL,
                 Date DATE NOT NULL,
                 Category TEXT NOT NULL,
                 Particular TEXT NOT NULL,
                 Amount REAL NOT NULL);''')

# FUNCTION TO INSERT DATA INTO TABLE 
def insert_data(enterprise, type_, item, date, category, particular, amount):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (Enterprise, Type, Item, Date, Category, Particular, Amount) VALUES (?,?,?,?,?,?,?)",
                  (enterprise, type_, item, date, category, particular, amount))
# SAVES THE NEW DATA TO THE TABLE
    conn.commit()
    print(f"Successfully inserted new data for {item} into the expenses table")

# CLOSES CONNECTION TO DATABASE
    conn.close()