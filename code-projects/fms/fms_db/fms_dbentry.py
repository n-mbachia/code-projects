import sqlite3

# FUNCTION TO INSERT DATA
def insert_data(conn):
    try:
        # CREATE CURSOR
        c = conn.cursor()
        # TAKE USER INPUT
        id = input("Enter ID: ")
        name = input("Enter name: ")
        date = input("Enter date: ")
        amount = input("Enter amount: ")
        item = input("Enter item: ")
        type = input("Enter type: ")
        category = input("Enter category: ")
        enterprise = input("Enter enterprise: ")
        # EXECUTE TO INSERT DATA
        c.execute("INSERT INTO Farm_Manager_System (id, name, date, amount, item, type, category, enterprise) VALUES(?,?,?,?,?,?,?,?)", (id, name, date, amount, item, type, category, enterprise))
        # SAVE TO DATABASE
        conn.commit()
        print('data inserted successfully')
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")

