import sqlite3

# CREATE TABLE
def create_table(conn):
    try:
	# CREATE CURSOR
        c = conn.cursor()
	# QUERY TO CREATE TABLE 'Farm_Manager_System"
        c.execute('''CREATE TABLE IF NOT EXISTS Farm_Manager_System 
                      (id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      date TEXT,
                      amount DECIMAL(10, 2) NOT NULL,
                      item TEXT,
                      type TEXT,
                      category TEXT,
		      enterprise TEXT);''')
        print('table created successfully')
    except Error as e:
        print(e)

