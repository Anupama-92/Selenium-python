from collections import defaultdict

# Default factory is int, so it defaults to 0
counts = defaultdict(int)
counts['a'] += 1
counts['b'] += 2
print(counts)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# Default factory is list, so it defaults to an empty list
list_dict = defaultdict(list)
list_dict['a'].append(1)
print(list_dict)  # Output: defaultdict(<class 'list'>, {'a': [1]})

# Grouping Items with defaultdict(list)

words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(grouped)
# Output: defaultdict(<class 'list'>, {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']})

# Using defaultdict(set) to Group Unique Items

names = [('Alice', 'Math'), ('Bob', 'Science'), ('Alice', 'Science'), ('Bob', 'Math')]
subjects = defaultdict(set)

for name, subject in names:
    subjects[name].add(subject)

print(subjects)
# Output: defaultdict(<class 'set'>, {'Alice': {'Math', 'Science'}, 'Bob': {'Science', 'Math'}})

# Using defaultdict for Accumulating Values

sales = [('apple', 10), ('banana', 5), ('apple', 15), ('banana', 10)]
total_sales = defaultdict(int)

for item, quantity in sales:
    total_sales[item] += quantity

print(total_sales)
# Output: defaultdict(<class 'int'>, {'apple': 25, 'banana': 15})

# Using defaultdict for Categorizing Data

numbers = [1, 2, 3, 4, 5, 6]
categorized = defaultdict(list)

for number in numbers:
    if number % 2 == 0:
        categorized['even'].append(number)
    else:
        categorized['odd'].append(number)

print(categorized)
# Output: defaultdict(<class 'list'>, {'odd': [1, 3, 5], 'even': [2, 4, 6]})

# Tracking Frequencies of Characters in a String

text = "hello world"
frequency = defaultdict(int)

for char in text:
    frequency[char] += 1

print(frequency)
# Output: defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Using defaultdict for Aggregation in Nested Structures

data = [{'city': 'NY', 'sales': 100}, {'city': 'LA', 'sales': 150}, {'city': 'NY', 'sales': 200}]
sales_by_city = defaultdict(int)

for record in data:
    sales_by_city[record['city']] += record['sales']

print(sales_by_city)
# Output: defaultdict(<class 'int'>, {'NY': 300, 'LA': 150})


