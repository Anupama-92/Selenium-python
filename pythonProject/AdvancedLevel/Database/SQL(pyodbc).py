import pyodbc

# Define the connection string
conn_string = (
    "Driver={SQL Server};"   
    "Server=192.168.0.30;"  
    "Database=Anupama;"  
    "Trusted_Connection=No;"  
    "UID=User11;PWD=CDev011@gfh;"
)

# Step 1: Establish a connection
conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

# Step 2: Execute a simple query
cursor.execute('SELECT * FROM Persons')

# Step 3: Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 4: Close the connection
conn.close()
