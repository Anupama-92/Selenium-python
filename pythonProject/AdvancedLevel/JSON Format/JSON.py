# JSON is a lightweight format for data exchange that is easy for humans to read and write, and for machines to parse and generate.
# JSON is a structured format, often used for configurations, data storage, and APIs.
import json
# Reading JSON file
with open('Sample_json.json',mode='r') as file:
    data = json.load(file)
    print(data)

# Writing to JSON file
data = {'name': 'Alice', 'age': 30}

with open('output.json', mode='w') as file:
    json.dump(data, file, indent=4)  # Indent for pretty formatting

# Converting JSON String to Python Dictionary:

json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)

print(data)  # Output: {'name': 'Alice', 'age': 30}

# Converting Python Dictionary to JSON String:
data = {'name': 'Alice', 'age': 30}
json_string = json.dumps(data, indent=4)

print(json_string)

# Stripping Whitespace and Slicing Keys in JSON
json_data = '''
{
    " name ": " Alice ",
    " age ": 30,
    " city ": " New York "
}
'''

# Loading JSON data
data = json.loads(json_data)

# Stripping whitespace from keys and values
cleaned_data = {key.strip(): str(value).strip() for key, value in data.items()}
print(cleaned_data)      # Output is {'name': 'Alice', 'age': '30', 'city': 'New York'}

# strip() is used on both keys and values to clean up extra spaces.
# Slicing a List Inside JSON

# JSON with a list
json_data1 = '''
{
    "users": ["Alice", "Bob", "Charlie", "David"]
}
'''

data = json.loads(json_data1)

# Slicing the first two users
users = data['users'][:2]
print(users)      # Output is ['Alice', 'Bob']








