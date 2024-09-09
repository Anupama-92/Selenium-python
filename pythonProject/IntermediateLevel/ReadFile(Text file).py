# Read Mode
# file = open('test.txt')
# print(file.read()) # Read entire file
# print(file.read(4))  # Read only 4 characters
# print(file.readline())  # Read only first line
# print(file.readlines())  # Reads all the lines and return them as each line a string element in a list.
# Write Mode
# file.write('abc')
# L = ["Anupama", "Selenium", "Python"]
# file.writelines(L)
file = open('geek.txt', 'w')
file.write("This is the write command \n")
file.write("It allows us to write in a particular file \n")
file.close()
# Append Mode
# file1 = open('test.txt')
# print(file1.read())
# # print(file1.write("Tomorrow \n"))
# file1.close()
# print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line=file.readline()

# values = [mobiles, washingmachines, refrigerators]
# for line in file.readline():
#     print(line)


#file.close()
# Reading Entire File:
with open('text.txt','r') as file:
  content = file.read()
  print(content)

# Reading Line by Line:
with open('text.txt','r') as file:
  for line in file:
    print(line)

# Reading Lines into a List:
with open('text.txt','r') as file:
  lines = file.readlines()
  for line in lines:
    print(line)

try:
    with open('filename.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print("An error occurred:", e)

# The strip() method is used to remove leading and trailing whitespaces, including newline characters (\n), from a string.

with open('text.txt','r') as file:
  for line in file:
    stripped_line = line.strip()
    print(stripped_line)

# The slice() function allows you to extract a portion of a string or a sequence.
with open('file2.txt', 'r') as file:
    content = file.read()
    sliced_content = content[:100]  # Get the first 100 characters
    print(sliced_content)

# The next() function retrieves the next item from the iterator.
with open('file3.txt', 'r') as file:
  line_iterator = iter(file)
  first_line = next(line_iterator)
  print(first_line)
  second_line = next(line_iterator)
  print(second_line)

# The seek() method is used to change the file pointer position within the file.
with open('filename.txt', 'r') as file:
    # Read the first 50 bytes
    content_part1 = file.read(50)
    print(content_part1)

    # Move the file pointer to the beginning
    file.seek(0)

    # Read the next 50 bytes
    content_part2 = file.read(50)
    print(content_part2)










# Open the text file in reading mode
with open('text.txt', 'r') as f:
  # Read all the lines of the text file into a list
  lines = f.readlines()
  # Iterate over the lines, and skip every other line
  for i in range(0, len(lines), 2):
    # Print the current line
    print(lines[i])

import csv

with open('in.csv', 'w') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row['first_name'], row['last_name'])


lines = [
    "  Hello, World!   ",
    "  Python is awesome!   ",
    "  Let's learn more!   "
]

# Create an iterator from the list of lines
iterator = iter(lines)

# Get the first line, strip the whitespace, and slice the first 5 characters
first_line = next(iterator).strip()[:5]
print(first_line)  # Output: 'Hello'

# Get the next line, strip the whitespace, and slice the first 6 characters
second_line = next(iterator).strip()[:6]
print(second_line)  # Output: 'Python'
