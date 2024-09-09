# Filter even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using filter with lambda to filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
# Converting the filter object to a list
even_numbers_list = list(even_numbers)
print(even_numbers_list)  # Output: [2, 4, 6, 8, 10]


# Filter strings longer than a certain length:
words = ["apple", "banana", "cherry", "date", "elderberry"]
# Using filter with lambda to filter strings longer than 5 characters
long_words = filter(lambda x: len(x) > 5, words)
# Converting the filter object to a list
long_words_list = list(long_words)
print(long_words_list)  # Output: ['banana', 'cherry', 'elderberry']


# Filter positive numbers from a list:
numbers = [-3, -2, -1, 0, 1, 2, 3]
# Using filter with lambda to filter positive numbers
positive_numbers = filter(lambda x: x > 0, numbers)
# Converting the filter object to a list
positive_numbers_list = list(positive_numbers)
print(positive_numbers_list)  # Output: [1, 2, 3]


# Filter vowels from a string:
sentence = "The quick brown fox jumps over the lazy dog"
# Using filter with lambda to filter vowels
vowels = filter(lambda x: x.lower() in 'aeiou', sentence)
# Converting the filter object to a list and joining the characters to form a string
vowels_string = ''.join(vowels)
print(vowels_string)  # Output: 'euiooueoaeo'


