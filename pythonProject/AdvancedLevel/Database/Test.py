import pymssql

conn = pymssql.connect(server='192.168.0.30', user='User11', password='CDev011@gfh', database='Anupama')

cursor = conn.cursor()
cursor.execute('SELECT 1')
row = cursor.fetchone()
print(row)

conn.close()