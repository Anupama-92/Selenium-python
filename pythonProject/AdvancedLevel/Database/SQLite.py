import sqlite3

# Step 1: Connect to an SQLite database (or create one)
conn = sqlite3.connect('test_database.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# # Step 4: Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Anupama', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Saranu', 25))

# Step 5: Commit the transaction
conn.commit()

# Step 6: Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 7: Close the connection
conn.close()
