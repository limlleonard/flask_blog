import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('flaskblog/site.db')
cursor = connection.cursor()

# Retrieve all table names in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]  # Each row contains a single column with the table name
    print(f"\nContents of table '{table_name}':")
    
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        column_names = [description[0] for description in cursor.description]
        print(" | ".join(column_names))
        
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"An error occurred with table {table_name}: {e}")

# Close the cursor and the connection
cursor.close()
connection.close()
