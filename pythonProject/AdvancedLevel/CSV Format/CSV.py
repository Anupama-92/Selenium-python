import csv

# Reading a CSV File:
with open('Python_learning.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to a CSV File:

data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading a CSV File into a Dictionary:
with open('Python_learning.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Writing a Dictionary to a CSV File:
data = [{'Name': 'Alice', 'Age': 30}, {'Name': 'Bob', 'Age': 25}]

with open('output.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


#  strip(), slice, and next() with CSV
# strip() is used to remove extra spaces around each value.
# next(reader) is used to skip the header row.

with open('Python_learning.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Using next() to skip headers
    for row in reader:
        # Stripping spaces from each cell
        row = [cell.strip() for cell in row]
        print(row)

# Slicing Rows from a CSV File

with open('Python_learning.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)[1:3]  # Slicing to get specific rows
    for row in rows:
        print(row)



