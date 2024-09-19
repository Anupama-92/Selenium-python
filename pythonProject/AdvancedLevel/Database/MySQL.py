import mysql.connector

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
)

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        salary FLOAT
    )
''')

# Step 4: Insert data
cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", ('John Doe', 55000.0))
cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", ('Jane Smith', 60000.0))

# Step 5: Commit the transaction
conn.commit()

# Step 6: Fetch data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 7: Close the connection
conn.close()
