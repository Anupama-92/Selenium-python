# Square each number in a list:
numbers = [1,2,3,4,5]
squared_numbers = map(lambda x:x**2, numbers)
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)

# Convert list of strings to uppercase:
strings = ["apple","banana","cherry"]
upper_strings = map(str.upper,strings)
upper_strings_list = list(upper_strings)
print(upper_strings_list)

# Combine two lists element-wise:
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
combined_numbers = map(lambda x,y:x+y, numbers1,numbers2)
combined_numbers_list = list(combined_numbers)
print(combined_numbers_list)

# Calculate lengths of strings in a list:
words = ["apple","banana","cherry"]
lengths = map(len, words)
lengths_list = list(lengths)
print(lengths_list)
