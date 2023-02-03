import argparse
import sqlite3

from fms_createdb import create_table
from fms_dbentry import insert_data
from fms_dbedit import edit_data 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--edit', action='store_true', help='Edit data in the database')
    args = parser.parse_args()
    
    conn = None
    try:
        # Create database connection
        conn = sqlite3.connect('fms.db')
        
        # Create table
        create_table(conn)
        
        # Insert data
        insert_data(conn)
        
        # View data
        view_data(conn)
        
        if args.edit:
            edit_data(conn)
        
    except KeyboardInterrupt:
        print("Keyboard Interrupt received, exiting...")
    finally:
        # Close connection
        if conn:
            conn.close()

if __name__ == '__main__':
    main()

