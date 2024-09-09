from collections import Counter

counter = Counter("Hello World")
print(counter)              # Output is Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})

print(counter.most_common(2))    # Output is [('l', 3), ('o', 2)]

#  Basic Usage of Counter to Count Elements in a List

fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
fruit_count = Counter(fruits)

print(fruit_count)
# Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Counting Characters in a String

text = "hello world"
char_count = Counter(text)

print(char_count)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Finding the Most Common Elements
numbers = [1, 2, 2, 3, 3, 3, 4]
number_count = Counter(numbers)

# Finding the most common elements
print(number_count.most_common(2))
# Output: [(3, 3), (2, 2)]

# Using Counter with Subtraction and Arithmetic Operations

counter_a = Counter(a=3, b=1)
counter_b = Counter(a=1, b=2)

# Addition
print(counter_a + counter_b)  # Output: Counter({'a': 4, 'b': 3})

# Subtraction
print(counter_a - counter_b)  # Output: Counter({'a': 2})

# Intersection (minimum counts)
print(counter_a & counter_b)  # Output: Counter({'a': 1, 'b': 1})

# Union (maximum counts)
print(counter_a | counter_b)  # Output: Counter({'a': 3, 'b': 2})

# Counting Words in a Sentence

sentence = "this is a test this is only a test"
word_count = Counter(sentence.split())

print(word_count)
# Output: Counter({'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1})

# Using Counter with a Dictionary

inventory = Counter({'apple': 5, 'banana': 2})

# Updating counts
inventory.update({'banana': 3, 'cherry': 4})

print(inventory)
# Output: Counter({'apple': 5, 'banana': 5, 'cherry': 4})

# Filtering Elements with Positive Counts

counter = Counter(a=2, b=-1, c=0, d=3)

# Filtering to include only positive counts
positive_counts = +counter

print(positive_counts)
# Output: Counter({'d': 3, 'a': 2})

# Removing Zero and Negative Counts

counter = Counter(a=3, b=0, c=-2, d=4)
counter += Counter()  # Remove zero and negative counts

print(counter)
# Output: Counter({'d': 4, 'a': 3})

# Counting Digits in a Number

number = 123445566
digit_count = Counter(str(number))

print(digit_count)
# Output: Counter({'4': 2, '5': 2, '6': 2, '1': 1, '2': 1, '3': 1})


