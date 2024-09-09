my_dict = {'a': 1, 'b': 2}
# Safe access with .get()
print(my_dict.get('a'))  # Output: 1
print(my_dict.get('c'))  # Output: None
print(my_dict.get('c', 'Not Found'))  # Output: Not Found
# Using get() to Avoid KeyError
inventory = {'apples': 10, 'bananas': 5}

# Attempting to access a missing key
print(inventory.get('oranges', 0))  # Output: 0

# Counting Occurrences with get()

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count_dict = {}

for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1

print(count_dict)  # Output: {'apple': 3, 'banana': 2, 'cherry': 1}

# Fetching Nested Dictionary Values Safely

data = {
    'person': {
        'name': 'Anupama',
        'address': {'city': 'Hyderabad'}
    }
}

# Accessing nested dictionary values
city = data.get('person', {}).get('address', {}).get('city', 'Unknown City')
print(city)  # Output: Hyderabad

# Using get() to Provide Default Settings

config = {'theme': 'dark', 'language': 'English'}

# Fetching with defaults
theme = config.get('theme', 'light')
font_size = config.get('font_size', 12)  # Default to 12 if not set

print(f"Theme: {theme}, Font Size: {font_size}")  # Output: Theme: dark, Font Size: 12

# Using get() to Handle Missing Translations

translations = {'hello': 'hola', 'bye': 'adiós'}

# Getting translation with default fallback
print(translations.get('hello', 'unknown'))  # Output: hola
print(translations.get('thanks', 'unknown'))  # Output: unknown

