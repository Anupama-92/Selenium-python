# Creating a List of Squares

squares = [x**2 for x in range(10)]
print(squares)        # output is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering with a Condition

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)      # Output is [0, 4, 16, 36, 64]

numbers = [1, 2, 3, 4, 5]
result = ['even' if x % 2 == 0 else 'Odd' for x in numbers]
print(result)    # Output is ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Nested List Comprehensions

pairs = [(x, y) for x in range(5) for y in range(5)]
print(pairs)   # Output is [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0),
# (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

# Modifying Items in the List

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # Output is ['HELLO', 'WORLD', 'PYTHON']


# List Comprehension with a Function

def square(x):
    return x*x


squares = [square(x) for x in range(10)]
print(squares)     # Output is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Flattening a List of Lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)   # Output is [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Removing Vowels from a String

sentence = "Hello, World!"
vowels = "aeiouAEIOU"
no_vowels = ''.join([char for char in sentence if char not in vowels])
print(no_vowels)   # Output is Hll, Wrld!

# Cartesian Product of Two Lists

colors = ['red', 'green', 'blue']
objects = ['ball', 'cube']
cartesian_product = [(color, obj) for color in colors for obj in objects]
print(cartesian_product)  # Output is [('red', 'ball'), ('red', 'cube'), ('green', 'ball'), ('green', 'cube'), ('blue', 'ball'), ('blue', 'cube')]


# Extracting Digits from a String

text = "abc123def456"
digits = [int(char) for char in text if char.isdigit()]
print(digits)      # Output is [1, 2, 3, 4, 5, 6]

# Generating a Dictionary from a List

names = ['Alice', 'Bob', 'Charlie']
name_length = {name: len(name) for name in names}
print(name_length)  # Output is {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Working with Tuples

points = [(1, 2), (3, 4), (5, 6)]
sums = [x+y for (x, y) in points]
print(sums)   # Output is [3, 7, 11]

# Transposing a Matrix - Using nested list comprehensions, we can transpose a matrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)     # Output is [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# Prime Numbers Using List Comprehension
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


primes = [x for x in range(2, 50) if is_prime(x)]
print(primes)    # Output is [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# Finding Common Elements Between Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [x for x in list1 if x in list2]
print(common_elements)     # Output is [4, 5]

# Creating a List of Tuples

numbers = [1, 2, 3, 4, 5]
squares = [(x, x**2) for x in numbers]
print(squares)  # Output is [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Filtering Strings by Length

words = ["hello", "world", "python", "is", "awesome"]
long_words = [word for word in words if len(word) > 5]
print(long_words)   # Output is ['python', 'awesome']

# Counting Occurrences of a Character in a List of Strings

sentences = ["hello", "world", "hello world"]
counts = [s.count('o') for s in sentences]
print(counts)     # Output is [1, 1, 2]

# Converting a List of Strings to Integers

str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = [int(x) for x in str_numbers]
print(str_numbers)   # Output is [1, 2, 3, 4, 5]

# Reversing Each String in a List

words = ["hello", "world", "python"]
reversed_words = [word[::-1] for word in words]
print(reversed_words)   # Output is ['olleh', 'dlrow', 'nohtyp']

# Removing Spaces from a List of Strings

sentences = ["hello world", "python is fun", "list comprehensions"]
no_spaces = [s.replace(" ", "") for s in sentences]
print(no_spaces)    # Output is ['helloworld', 'pythonisfun', 'listcomprehensions']

# Creating a List of ASCII Values
text = "hello"
ascii_values = [ord(char) for char in text]
print(ascii_values)  # Output is [104, 101, 108, 108, 111]

# Flattening a List of Tuples

pairs = [(1, 2), (3, 4), (5, 6)]
flattened = [item for pair in pairs for item in pair]
print(flattened)   # Output is [1, 2, 3, 4, 5, 6]


# Creating a List of Random Numbers
import random
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)



