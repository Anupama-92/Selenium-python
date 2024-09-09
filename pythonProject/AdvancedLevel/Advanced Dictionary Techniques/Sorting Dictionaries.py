from collections import OrderedDict

my_dict = {'b': 2, 'a': 1, 'c': 3}

# Sort by keys
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)  # Output: {'a': 1, 'b': 2, 'c': 3}


# Sorting by Values in Descending Order

sorted_by_values_desc = dict(sorted(my_dict.items(),key=lambda item: item[1], reverse=True))
print(sorted_by_values_desc)              # Output: {'a': 1, 'c': 2, 'b': 3}

# Sorting by Keys in Descending Order

sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
print(sorted_by_keys_desc)                # Output: {'c': 2, 'b': 3, 'a': 1}

# Sorting a Dictionary by the Length of Keys
my_dict1 = {'banana': 3, 'apple': 1, 'pear': 2}
sorted_by_key_length = dict(sorted(my_dict1.items(), key=lambda item: len(item[0])))
print(sorted_by_key_length)              # Output: {'pear': 2, 'apple': 1, 'banana': 3}


# Sorting a Nested Dictionary by a Sub-Value(Age)
nested_dict = {'person1': {'name': 'Alice', 'age': 25},
               'person2': {'name': 'Bob', 'age': 20},
               'person3': {'name': 'Charlie', 'age': 23}}

sorted_nested_dict = dict(sorted(nested_dict.items(), key=lambda item: item[1]['age']))

print(sorted_nested_dict)
# Output: {'person2': {'name': 'Bob', 'age': 20}, 'person3': {'name': 'Charlie', 'age': 23}, 'person1': {'name': 'Alice', 'age': 25}}

# Sorting a Dictionary by Multiple Criteria
my_dict2 = {'b': 3, 'a': 3, 'c': 2, 'd': 2}
sorted_by_value_then_key = dict(sorted(my_dict2.items(), key=lambda item: (item[1], item[0])))
print(sorted_by_value_then_key)  # Output: {'c': 2, 'd': 2, 'a': 3, 'b': 3}

# Sorting a Dictionary with OrderedDict
my_dict3 = {'b': 3, 'a': 1, 'c': 2}
ordered_dict = OrderedDict(sorted(my_dict3.items()))
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 3), ('c', 2)])

# Sorting a Dictionary by Custom Function


def custom_sort(item):
    # Custom rule: Sort by even values first, then by keys
    return item[1] % 2, item[0]


sorted_by_custom = dict(sorted(my_dict.items(), key=custom_sort))

print(sorted_by_custom)  # Output: {'a': 1, 'c': 2, 'b': 3}

# Sorting Dictionary Keys or Values Separately

sorted_keys = sorted(my_dict3.keys())
sorted_values = sorted(my_dict3.values())

print(sorted_keys)   # Output: ['a', 'b', 'c']
print(sorted_values) # Output: [1, 2, 3]
