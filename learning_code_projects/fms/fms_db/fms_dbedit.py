def edit_data(conn):
    try:
        # CREATE CURSOR
        c = conn.cursor()

        # TAKE USER INPUT
        id = input("Enter the ID of the entry you want to edit: ")
        column = input("Enter the column name you want to edit: ")
        new_value = input("Enter the new value for the column: ")

        # EXECUTE SQL QUERY TO UPDATE COLUMN
        c.execute(f"UPDATE Farm_Manager_System SET {column} = ? WHERE id = ?", (new_value, id))

        # COMMIT CHANGES TO DATABASE
        conn.commit()

        print(f"Data with id {id} has been updated successfully.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def main():
    # CONNECT TO DATABASE
    conn = sqlite3.connect('fms.db')

    # CREATE TABLE
    create_table(conn)

    while True:
        # TAKE USER COMMAND
        command = input("Enter command (edit, view, exit): ")

        if command == "edit":
            edit_data(conn)
        elif command == "view":
            view_data(conn)
        elif command == "exit":
            break
        else:
            print("Invalid command. Please enter a valid command.")

    # CLOSE CONNECTION
    conn.close()


