import pymssql

# Step 1: Establish a connection
conn = pymssql.connect(
    server='192.168.0.30',  # Replace with your server name or IP
    user='User11',  # Replace with your username
    password='CDev011@gfh',  # Replace with your password
    database='Anupama'  # Replace with your database name
)

cursor = conn.cursor()

# Step 2: Execute a simple query
cursor.execute('SELECT * FROM Persons')  # Replace with your table name

# Step 3: Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 4: Close the connection
conn.close()
