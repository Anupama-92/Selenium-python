# Using Built-in Strings method;
# Simple search and replace
original_string = "Hello, World!"
new_string = original_string.replace("World", "Python")
print(new_string)

# Using Regular Expressions:
import re

# Search and replace using regular expressions
original_string = "Hello, World!"
new_string = re.sub(r'World', 'Python', original_string)
print(new_string)

# Replacing with Groups using Regular Expressions:

# Replace with groups using regular expressions
original_string = "Hello, John Doe!"
new_string = re.sub(r'Hello, (\w+) (\w+)!', r'Goodbye, \2!', original_string)
print(new_string)

# Using a Function for Replacement:


# Using a function for replacement
def replace_func(match):
    return match.group(0).upper()

original_string = "hello, world!"
new_string = re.sub(r'\b\w+\b', replace_func, original_string)
print(new_string)

# Replacing Case Insensitively:
# Case-insensitive search and replace
original_string = "Hello, world!"
new_string = re.sub(r'hello', 'Python', original_string, flags=re.IGNORECASE)
print(new_string)
