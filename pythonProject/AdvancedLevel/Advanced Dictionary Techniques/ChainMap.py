from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)

print(chain['a'])  # Output: 1 (from dict1)
print(chain['b'])  # Output: 2 (from dict1)
print(chain['c'])  # Output: 4 (from dict2)

# Adding a new dictionary to the chain
dict3 = {'d': 5}
chain = chain.new_child(dict3)
print(chain['d'])  # Output: 5

# Modifying ChainMap Data

dict1 = {'x': 10, 'y': 20}
dict2 = {'y': 30, 'z': 40}

# Combine with ChainMap
chain = ChainMap(dict1, dict2)

# Modifying values affects the first dictionary (dict1)
chain['x'] = 100
chain['y'] = 200

print(dict1)  # Output: {'x': 100, 'y': 200}
print(dict2)  # Output: {'y': 30, 'z': 40}

# Using ChainMap for Variable Scoping

global_scope = {'var': 'global'}
local_scope = {'var': 'local'}

# Chain the local scope first, then global
scope = ChainMap(local_scope, global_scope)

print(scope['var'])  # Output: 'local' (local scope is checked first)

# Using ChainMap to Aggregate Dictionaries with Shared Keys

data1 = {'a': 1, 'b': 2}
data2 = {'b': 3, 'c': 4}

# Combine with ChainMap
combined_data = ChainMap(data1, data2)

# Iterate over all keys
for key, value in combined_data.items():
    print(key, value)
# Output:
# a 1
# b 2
# c 4

# Reversing the Order of ChainMap

dict_a = {'key': 'from A'}
dict_b = {'key': 'from B'}

# Normal order: dict_a first
chain = ChainMap(dict_a, dict_b)
print(chain['key'])  # Output: 'from A'

# Reverse order: dict_b first
reversed_chain = ChainMap(dict_b, dict_a)
print(reversed_chain['key'])  # Output: 'from B'

# Flattening a ChainMap into a Single Dictionary

dict1 = {'a': 1}
dict2 = {'b': 2}
chain = ChainMap(dict1, dict2)

# Flatten the ChainMap into a single dictionary
flattened = dict(chain)

print(flattened)  # Output: {'a': 1, 'b': 2}


