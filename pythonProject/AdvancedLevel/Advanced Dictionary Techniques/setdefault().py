my_dict = {'a': 1, 'b': 2}
my_dict.setdefault('c', 3)  # Adds 'c' with a default value of 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Using setdefault to add a default value if the key is missing
my_dict1 = {'name':'Alice'}
# Attempt to retrieve the key 'age'. If not found, insert 'age': 25
age = my_dict1.setdefault('age', 25)

print(my_dict1)  # Output: {'name': 'Alice', 'age': 25}
print(age)      # Output: 25

# Using setdefault() Without a Default Value
age = my_dict1.setdefault('age')
print(my_dict1)  # Output: {'name': 'Alice', 'age': None}
print(age)      # Output: None

# Counting Occurrences Using setdefault()
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = {}

for word in words:
    # Increment the count of each word, setting it to 0 initially if not found
    word_count[word] = word_count.setdefault(word, 0) + 1

print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# Creating Nested Dictionaries

nested_dict = {}

# Adding nested keys safely
nested_dict.setdefault('users', {}).setdefault('Alice', {}).setdefault('age', 25)

print(nested_dict)  # Output: {'users': {'Alice': {'age': 25}}}

# Grouping Items Using setdefault()

data = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'orange')]
grouped = {}

for category, item in data:
    # Append item to the list under the category, creating the list if not found
    grouped.setdefault(category, []).append(item)

print(grouped)  # Output: {'fruit': ['apple', 'banana', 'orange'], 'vegetable': ['carrot']}

# Using setdefault() for Accumulating Results

results = {}

# Simulate adding values for multiple keys
for key, value in [('group1', 10), ('group2', 20), ('group1', 30)]:
    results.setdefault(key, []).append(value)

print(results)  # Output: {'group1': [10, 30], 'group2': [20]}




