squares = {x:x*x for x in range(1,6)}
print(squares)                       # Output is {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)                        # Output is {1: 'a', 2: 'b', 3: 'c'}

# Filtering During Comprehension

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
even_numbers = {key: value for key, value in numbers.items() if value % 2 == 0}

print(even_numbers)  # Output: {'two': 2, 'four': 4}

# Swapping Keys and Values
original_dict = {'apple': 5, 'banana': 3, 'cherry': 7}
swapped_dict = {value: key for key, value in original_dict.items()}

print(swapped_dict)  # Output: {5: 'apple', 3: 'banana', 7: 'cherry'}

# Creating a Dictionary from Two Lists

keys = ['a', 'b', 'c']
values = [1, 2, 3]
merged_dict = {key: value for key, value in zip(keys, values)}

print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Using Conditional Logic in Comprehensions

numbers = range(1, 6)
condition_dict = {num: ('even' if num % 2 == 0 else 'odd') for num in numbers}

print(condition_dict)  # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# Aggregating Counts with Comprehensions

letters = ['a', 'b', 'a', 'c', 'b', 'a']
count_dict = {letter: letters.count(letter) for letter in set(letters)}

print(count_dict)  # Output: {'a': 3, 'c': 1, 'b': 2}

# Dictionary Comprehension with Multiple Iterables

keys = ['x', 'y']
values = [10, 20, 30]
nested_dict = {k: v for k in keys for v in values}

print(nested_dict)  # Output: {'x': 30, 'y': 30} (last value overrides previous)

# Using Functions in Comprehensions


def square(x):
    return x * x


numbers = range(1, 4)
squared_dict = {num: square(num) for num in numbers}

print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9}

# Combining Dictionary Comprehensions with enumerate()

fruits = ['apple', 'banana', 'cherry']
index_dict = {index: fruit for index, fruit in enumerate(fruits)}

print(index_dict)  # Output: {0: 'apple', 1: 'banana', 2: 'cherry'}
