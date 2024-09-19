import psycopg2

# Step 1: Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="test_db",
    user="postgres",
    password="password"
)

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        price DECIMAL(10, 2)
    )
''')

# Step 4: Insert data
cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ('Laptop', 1200.50))
cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ('Smartphone', 800.00))

# Step 5: Commit the transaction
conn.commit()

# Step 6: Fetch data
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 7: Close the connection
conn.close()
