import sqlite3
from datetime import datetime

def view_data_by_type(conn, type):
    try:
        # CREATE CURSORr
        c = conn.cursor()
        # execute sql command to view data filtered by type
        c.execute("SELECT * FROM Farm_Manager_System WHERE type = ?", (type,))
        rows = c.fetchall()
        # lOOP THROUGH ROWS AND OUTPUT DATA
        for row in rows:
            print(row)
    except Error as e:
        print(e)

# OUTPUTS ALL DATA
def view_all_data(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Farm_Manager_System")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
# OUTPUT        
conn = sqlite3.connect("fms.db")
view_all_data(conn)
conn.close()

# SUMMARY VIEW
def summary_by_month_and_type(conn):
    c = conn.cursor()
    
    # QUERY EXECUTE
    c.execute('''SELECT strftime('%m', date) as month, type, SUM(amount), enterprise
                FROM Farm_Manager_System
                GROUP BY month, type, enterprise
                ORDER BY month''')
    data = c.fetchall()
    
    # PRINT DATAa
    for row in data:
        print(f"Month: {row[0]}, Type: {row[1]}, Total Amount: {row[2]}, Enterprise: {row[3]}")

conn = sqlite3.connect('fms.db')
summary_by_month_and_type(conn)
conn.close()

