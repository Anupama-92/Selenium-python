my_dict = {'a': 1, 'b': 2, 'c': 3}

# Removing specific key
value = my_dict.pop('a')
print(value)  # Output: 1
print(my_dict)  # Output: {'b': 2, 'c': 3}

# Removing last item
last_item = my_dict.popitem()
print(last_item)  # Output: ('c', 3)
print(my_dict)  # Output: {'b': 2}

# Using pop() with a Default Value

my_dict1 = {'a': 1, 'b': 2}

# Attempt to remove the key 'c'; if not found, return 0
value = my_dict1.pop('c', 0)

print(my_dict1)  # Output: {'a': 1, 'b': 2}
print(value)    # Output: 0

# Handling Key Errors with pop()

my_dict2 = {'x': 10, 'y': 20}

# Attempting to pop a non-existent key without default will raise a KeyError
try:
    my_dict2.pop('z')
except KeyError as e:
    print(f"Error: {e}")  # Output: Error: 'z'

# Using popitem() on an Empty Dictionary

empty_dict = {}

# Attempting to pop an item from an empty dictionary raises a KeyError
try:
    empty_dict.popitem()
except KeyError as e:
    print(f"Error: {e}")  # Output: Error: 'popitem(): dictionary is empty'

# Sequential Use of popitem()

my_dict3 = {'x': 100, 'y': 200, 'z': 300}

# Sequentially remove items from the dictionary
print(my_dict3.popitem())  # Output: ('z', 300)
print(my_dict3.popitem())  # Output: ('y', 200)
print(my_dict3.popitem())  # Output: ('x', 100)

print(my_dict3)  # Output: {}

# Combining pop() and popitem() in a Workflow

inventory = {'apples': 5, 'bananas': 3, 'oranges': 8}

# Removing a specific item using pop
apples_count = inventory.pop('apples')
print(f"Removed apples: {apples_count}")  # Output: Removed apples: 5

# Removing the last item using popitem
last_item = inventory.popitem()
print(f"Last item removed: {last_item}")  # Output: Last item removed: ('oranges', 8)

print(inventory)  # Output: {'bananas': 3}

