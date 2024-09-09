# Python 3.5+ way of merging
from collections import ChainMap
from functools import reduce

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)

# Python 3.9+ way of merging
merged = dict1 | dict2
print(merged)


# Using update() Method
# Merging dict2 into dict1 (dict1 is updated in place)
dict1.update(dict2)

print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using collections.ChainMap - Viewing multiple dictionaries as one using ChainMap

dict3 = {'key1': 'value1'}
dict4 = {'key2': 'value2'}
dict5 = {'key1': 'overwritten', 'key3': 'value3'}

# Creating a combined view
combined = ChainMap(dict1, dict2, dict3)

print(combined)           # Output: ChainMap({'key1': 'value1'}, {'key2': 'value2'}, {'key1': 'overwritten', 'key3': 'value3'})
print(combined['key1'])   # Output: value1 (takes the first match)

# Using Dictionary Comprehension for Custom Merging

# Example: Custom merging using dictionary comprehension
dict6 = {'a': 10, 'b': 20}
dict7 = {'b': 5, 'c': 15}

# Custom merging: add values if the key exists in both
merged_dict = {key: dict6.get(key, 0) + dict7.get(key, 0) for key in set(dict6) | set(dict7)}

print(merged_dict)  # Output: {'a': 10, 'b': 25, 'c': 15}

# Using zip() with dict() for Key-Value Pair Merging
# When we have a separate lists of keys and values, we can merge them into a dictionary using zip().
# Merging using dict constructor and zip()
keys = ['one', 'two', 'three']
values = [1, 2, 3]

# Creating a dictionary from keys and values
merged_dict = dict(zip(keys, values))

print(merged_dict)  # Output: {'one': 1, 'two': 2, 'three': 3}

# Merging Dictionaries with functools.reduce()

dict8 = {'a': 1, 'b': 2}
dict9 = {'b': 3, 'c': 4}
dict10 = {'c': 5, 'd': 6}

# Merging all dictionaries into one
merged_dict = reduce(lambda d8, d9: {**d8, **d9}, [dict8, dict9, dict10])

print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 5, 'd': 6}

# Handling Key Conflicts with Custom Functions


def merge_dicts(d1, d2):
    merged = d1.copy()  # Start with a copy of the first dictionary
    for key, value in d2.items():
        if key in merged:
            merged[key] += value  # Custom rule: sum values if key exists
        else:
            merged[key] = value
    return merged


dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}

# Using the custom function to merge
merged_dict = merge_dicts(dict1, dict2)


