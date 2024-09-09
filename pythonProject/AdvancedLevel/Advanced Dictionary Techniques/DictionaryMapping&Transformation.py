# Example: Transform values
my_dict = {'a': 1, 'b': 2, 'c': 3}
transformed = {k: v ** 2 for k, v in my_dict.items()}  # Squaring values
print(transformed)  # Output: {'a': 1, 'b': 4, 'c': 9}

# Transforming Keys and Values
my_dict = {'a': 1, 'b': 2, 'c': 3}
transformed_dict = {k.upper(): -v for k,v in my_dict.items()}
print(transformed_dict)                    # Output: {'A': -1, 'B': -2, 'C': -3}

# Filtering Dictionary Elements
my_dict = {'a': 1, 'b': 2, 'c': 3}
filtered_dict = {k: v for k, v in my_dict.items() if v>1}
print(filtered_dict)                # Output: {'b': 2, 'c': 3}

# Applying Functions to Values


def double(x):
    return x * 2


my_dict = {'a': 1, 'b': 2, 'c': 3}
doubled_values = {k: double(v) for k, v in my_dict.items()}
print(doubled_values)  # Output: {'a': 2, 'b': 4, 'c': 6}

# Combining Two Dictionaries by Mapping

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'c': 6}

combined_dict = {k: dict1[k] + dict2[k] for k in dict1.keys()}
print(combined_dict)  # Output: {'a': 5, 'b': 7, 'c': 9}

# Transforming Nested Dictionaries

# Example: Increment all numeric values in a nested dictionary by 1
nested_dict = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}


def increment_values(d):
    for k, v in d.items():
        if isinstance(v, dict):  # If the value is a dictionary, apply recursively
            increment_values(v)
        else:  # Otherwise, increment the value
            d[k] = v + 1
    return d


incremented_dict = increment_values(nested_dict)
print(incremented_dict)  # Output: {'a': 2, 'b': {'c': 3, 'd': 4}, 'e': 5}

# Using map() to Transform Values

# Convert all values to strings
my_dict = {'a': 1, 'b': 2, 'c': 3}
transformed_values = dict(map(lambda item: (item[0], str(item[1])), my_dict.items()))
print(transformed_values)  # Output: {'a': '1', 'b': '2', 'c': '3'}

# Merging Dictionaries with Value Mapping
# Multiply the values of common keys from two dictionaries
dict1 = {'a': 2, 'b': 3, 'c': 4}
dict2 = {'a': 5, 'b': 6, 'd': 7}

merged_dict = {k: dict1.get(k, 1) * dict2.get(k, 1) for k in dict1.keys() | dict2.keys()}
print(merged_dict)  # Output: {'a': 10, 'b': 18, 'c': 4, 'd': 7}

# Grouping Elements by Key Using defaultdict
from collections import defaultdict

# Example: Group words by their length
words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
grouped = defaultdict(list)

for word in words:
    grouped[len(word)].append(word)

print(dict(grouped))  # Output: {5: ['apple', 'grape'], 6: ['banana', 'cherry'], 4: ['date', 'fig']}

# Data Transformation for APIs

# Example: Rename keys from an API response to internal model keys
api_response = {'userName': 'john_doe', 'userAge': 30}
key_mapping = {'userName': 'name', 'userAge': 'age'}

transformed_data = {key_mapping[k]: v for k, v in api_response.items()}
print(transformed_data)  # Output: {'name': 'john_doe', 'age': 30}

# Config Management and Parsing
# Merging configuration dictionaries
default_config = {'host': 'localhost', 'port': 8080, 'debug': False}
env_config = {'port': 9090, 'debug': True}  # Environment-specific overrides

merged_config = {**default_config, **env_config}
print(merged_config)  # Output: {'host': 'localhost', 'port': 9090, 'debug': True}

# Applying Business Logic to Data

# Apply discount based on category
products = {'apple': ('fruit', 100), 'banana': ('fruit', 50), 'carrot': ('vegetable', 30)}
discounts = {'fruit': 0.1, 'vegetable': 0.2}

# Apply discount based on category
discounted_prices = {k: v[1] * (1 - discounts[v[0]]) for k, v in products.items()}
print(discounted_prices)  # Output: {'apple': 90.0, 'banana': 45.0, 'carrot': 24.0}


