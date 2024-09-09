from collections import OrderedDict

ordered = OrderedDict()
ordered['apple'] = 3
ordered['Banana'] = 2
ordered['Cherry'] = 5
print(ordered)                  # Output: OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5)])
ordered.move_to_end('Banana')   # Moves 'banana' to the end
print(ordered)                  # Output: OrderedDict([('apple', 3), ('cherry', 5), ('banana', 2)])

# Reordering the elements

# Initial OrderedDict
ordered_dict = OrderedDict([('one', 1), ('two', 2), ('three', 3)])

# Moving 'two' to the end
ordered_dict.move_to_end('two')

print(ordered_dict)  # Output: OrderedDict([('one', 1), ('three', 3), ('two', 2)])

# Moving 'one' to the beginning
ordered_dict.move_to_end('one', last=False)

print(ordered_dict)  # Output: OrderedDict([('one', 1), ('three', 3), ('two', 2)])

# Sorting OrderedDict by Keys or Values

ordered_dict = OrderedDict([('apple', 3), ('banana', 1), ('cherry', 2)])
# Sorting by values
sorted_by_value = OrderedDict(sorted(ordered_dict.items(), key=lambda item: item[1]))
print(sorted_by_value)  # Output: OrderedDict([('banana', 1), ('cherry', 2), ('apple', 3)])

# Sorting by keys
sorted_by_key = OrderedDict(sorted(ordered_dict.items(), key=lambda item: item[0]))
print(sorted_by_key)  # Output: OrderedDict([('apple', 3), ('banana', 1), ('cherry', 2)])

# Reversing an OrderedDict
ordered_dict = OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Reversing the OrderedDict
reversed_dict = OrderedDict(reversed(ordered_dict.items()))

print(reversed_dict)  # Output: OrderedDict([('third', 3), ('second', 2), ('first', 1)])

# Maintaining Consistent Order During Data Processing

# Data processing with consistent order
data = [('id', 1), ('name', 'Alice'), ('age', 30)]
ordered_data = OrderedDict(data)

# Modifying the order
ordered_data.move_to_end('id')

print(ordered_data)  # Output: OrderedDict([('name', 'Alice'), ('age', 30), ('id', 1)])

# Comparing OrderedDicts
# Creating two OrderedDicts with the same items but different orders
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])

# Comparing OrderedDicts
print(od1 == od2)  # Output: False


# Combining OrderedDicts While Preserving Order

od1 = OrderedDict([('one', 1), ('two', 2)])
od2 = OrderedDict([('three', 3), ('four', 4)])

# Merging them while preserving order
combined = OrderedDict(list(od1.items()) + list(od2.items()))

print(combined)  # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])


