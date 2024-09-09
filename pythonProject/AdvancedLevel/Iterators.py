class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


my_range = MyRange(1, 5)
for num in my_range:
    print(num)


# Iterator for Fibonacci Sequence

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib


fib = Fibonacci(50)
for num in fib:
    print(num)

# Iterator for Reversing a String

class ReverseString:
    def __init__(self, string):
        self.string = string
        self.index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.string[self.index]


reverse_iter = ReverseString("hello")
for char in reverse_iter:
    print(char)               # Output is olleh

# Creating an Infinite Iterator


class InfiniteIterator:
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current


infinite_iter = InfiniteIterator(10)
for _ in range(5):
    print(next(infinite_iter))            # Output is 11, 12, 13, 14, 15


# Custom Iterator for a List

class StepIterator:
    def __init__(self, data, step=1):
        self.data = data
        self.index = 0
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += self.step
        return value


step_iter = StepIterator([1, 2, 3, 4, 5, 6], step=2)
for num in step_iter:
    print(num)                                                   # Output is 1, 3, 5

# Iterator with Conditional Logic


class EvenIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            if value % 2 == 0:
                return value
        raise StopIteration


even_iter = EvenIterator([1, 2, 3, 4, 5, 6])

for num in even_iter:
    print(num)               # Output is 2 4 6

# Iterator for Dictionary Items


class DictIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        self.index += 1
        return (key, self.dictionary[key])


my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_iter = DictIterator(my_dict)

for key, value in dict_iter:
    print(key, value)


# Chaining Iterators

class ChainIterator:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.current_iter = iter(self.iterables[0])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.current_iter)
        except StopIteration:
            self.index += 1
            if self.index >= len(self.iterables):
                raise StopIteration
            self.current_iter = iter(self.iterables[self.index])
            return next(self)


iter1 = iter([1, 2, 3])
iter2 = iter(['a', 'b', 'c'])
chain_iter = ChainIterator(iter1, iter2)

for item in chain_iter:
    print(item)

# Reverse Iterator


class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # Start from the end of the list

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration  # Stop when we've reached the beginning of the list
        self.index -= 1
        return self.data[self.index]


my_list = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(my_list)

for item in reverse_iter:
    print(item)                      # Output is 5 4 3 2 1

# Infinite Iterator


class InfiniteEvenIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        even = self.current
        self.current += 2
        return even


even_iter = InfiniteEvenIterator()

for i in range(5):  # To avoid an infinite loop, we use a range
    print(next(even_iter))














