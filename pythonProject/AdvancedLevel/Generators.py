# Basic Generator


def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration

# Using Generators in loop


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for count in countdown(5):    # Output is 5 4 3 2 1
    print(count)

# Generator Expressions

gen_exp = (x**2 for x in range(5))

for value in gen_exp:
    print(value)                 # Output is 0 1 4 9 16

# Reading a Large File Line by Line


def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


for line in read_large_file('large_file.txt'):
    print(line)


# Fibonacci Sequence Generator

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


fib_gen = fibonacci()
for _ in range(10):  # Print the first 10 Fibonacci numbers
    print(next(fib_gen))               # Output is 0 1 1 2 3 5 8 13 21 34


# Generator with a Loop

def squares(n):
    for i in range(1, n+1):
        yield i*i


squares_gen = squares(5)
for square in squares_gen:
    print(square)        # Output is 1 4 9 16 25


# Using yield in a Loop


def items_generator(items):
    for item in items:
        yield item


items = ["Apple", "Banana", "Orange"]
gen = items_generator(items)

for item in gen:
    print(item)

# Chaining Generators


def generator1():
    yield from range(3)  # Yields 0, 1, 2


def generator2():
    yield from generator1()
    yield from range(3, 6)  # Yields 3, 4, 5


for value in generator2():
    print(value)

# Filtering Data with Generators


def filter_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


numbers = [1, 2, 3, 4, 5, 6]
even_gen = filter_even(numbers)

for even in even_gen:
    print(even)         # Output is 2, 4, 6

# Prime Number Generator


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


primes = prime_generator()
for _ in range(10):  # Print the first 10 prime numbers
    print(next(primes))      # Output is 2 3 5 7 11 13 17 19 23 29


# Generator for Chunking a List

def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunks = chunk_list(data, 3)

for chunk in chunks:
    print(chunk)   # Output is [1, 2, 3], [4, 5, 6], [7, 8, 9]

# Processing data in stages.

def stage_one(data):
    for item in data:
        if item % 2 == 0:
            yield item

def stage_two(data):
    for item in data:
        yield item * 2

data = range(10)
pipeline = stage_two(stage_one(data))

for item in pipeline:
    print(item)




