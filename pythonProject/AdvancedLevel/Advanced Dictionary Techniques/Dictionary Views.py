my_dict = {'a': 1, 'b': 2, 'c': 3}

# View of keys
keys_view = my_dict.keys()
print(keys_view)  # Output: dict_keys(['a', 'b', 'c'])

# View of values
values_view = my_dict.values()
print(values_view)  # Output: dict_values([1, 2, 3])

# View of items
items_view = my_dict.items()
print(items_view)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Modifying the dictionary affects the views
my_dict['d'] = 4
print(keys_view)  # Output: dict_keys(['a', 'b', 'c', 'd'])

# Iterating Over Dictionary Views

my_dict1 = {'x': 10, 'y': 20, 'z': 30}

# Iterating over keys
for key in my_dict1.keys():
    print(f"Key: {key}")

# Iterating over values
for value in my_dict1.values():
    print(f"Value: {value}")

# Iterating over items (key-value pairs)
for key, value in my_dict1.items():
    print(f"{key}: {value}")

# Output:
# Key: x
# Key: y
# Key: z
# Value: 10
# Value: 20
# Value: 30
# x: 10
# y: 20
# z: 30

# Dictionary Views Reflect Changes Dynamically
my_dict2 = {'one': 1, 'two': 2}

# Accessing views
items_view = my_dict2.items()

print(items_view)  # Output: dict_items([('one', 1), ('two', 2)])

# Modifying the dictionary
my_dict2['three'] = 3

# The view reflects the change
print(items_view)  # Output: dict_items([('one', 1), ('two', 2), ('three', 3)])

# Removing an item
del my_dict2['one']

print(items_view)  # Output: dict_items([('two', 2), ('three', 3)])

# Set Operations on Dictionary Views

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# Getting keys views
keys_view1 = dict1.keys()
keys_view2 = dict2.keys()

# Set operations
intersection = keys_view1 & keys_view2  # Common keys
union = keys_view1 | keys_view2         # All keys combined
difference = keys_view1 - keys_view2    # Keys in dict1 not in dict2

print(intersection)  # Output: {'b', 'c'}
print(union)         # Output: {'a', 'b', 'c', 'd'}
print(difference)    # Output: {'a'}

# Using Views to Check Membership Efficiently

my_dict3 = {'cat': 4, 'dog': 4, 'spider': 8}

# Checking if a key exists
if 'dog' in my_dict3.keys():
    print("Dog is in the dictionary.")  # Output: Dog is in the dictionary.

# Checking if a value exists
if 8 in my_dict3.values():
    print("An animal with 8 legs exists.")  # Output: An animal with 8 legs exists.

# Converting Views to Lists for Further Manipulation
my_dict4 = {'x': 100, 'y': 200, 'z': 300}

# Converting keys and values views to lists
keys_list = list(my_dict4.keys())
values_list = list(my_dict4.values())
items_list = list(my_dict4.items())

print(keys_list)    # Output: ['x', 'y', 'z']
print(values_list)  # Output: [100, 200, 300]
print(items_list)   # Output: [('x', 100), ('y', 200), ('z', 300)]

# Synchronizing Two Dictionaries Using Views

dict_a = {'name': 'Alice', 'age': 30}
dict_b = {'age': 28, 'city': 'New York'}

# Keeping only keys present in both dictionaries
common_keys = dict_a.keys() & dict_b.keys()

# Updating dict_a with values from dict_b for common keys
for key in common_keys:
    dict_a[key] = dict_b[key]

print(dict_a)  # Output: {'name': 'Alice', 'age': 28}

