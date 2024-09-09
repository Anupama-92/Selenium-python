# Simple Grouping:
import re

# Match a date string in the format "dd-mm-yyyy"
date_string = "Today's date is 24-05-2024"
match = re.search(r'(\d{2})-(\d{2})-(\d{4})', date_string)
if match:
    day, month, year = match.groups()
    print("Day:", day)
    print("Month:", month)
    print("Year:", year)

# Named Grouping:
# Match a name and age from a string
text = "Name: John, Age: 30"
match = re.search(r'Name: (?P<name>\w+), Age: (?P<age>\d+)', text)
if match:
    print("Name:", match.group('name'))
    print("Age:", match.group('age'))


# Nested Grouping:
# Match a HTML tag and its content
html_text = "<div><p>Hello, <b>world</b>!</p></div>"
match = re.search(r'<(\w+)>(.*?)</\1>', html_text)
if match:
    print("Tag:", match.group(1))
    print("Content:", match.group(2))

# Non-Capturing Group:
# Match a phone number with area code (capturing area code)
phone_number = "Phone: (123) 456-7890"
match = re.search(r'(\(\d{3}\)) (\d{3}-\d{4})', phone_number)
if match:
    print("Area Code:", match.group(1))
    print("Phone Number:", match.group(2))