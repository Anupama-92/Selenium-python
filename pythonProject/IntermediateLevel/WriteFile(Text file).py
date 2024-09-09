# The islice() function is a built-in function in Python that can be used to iterate over a sequence, skipping the first few elements.
# Next function is used to skip the line
# seek() function to move the file pointer to a specific position in the file and skip over lines that way:


# Read the file and store all the lines in list
# Reverse the list
# Write the list back to the file

# Writing to a File:
with open('text.txt','w') as file:
    file.write("Hello, world!")
# Appending to a File:
with open('text.txt','a') as file:
    file.write("Hello world!")





with open('test.txt', 'r') as reader:
    content = reader.readline()   # Amazon is the best online shopping, Flipkart is the Online shopping
    reversed(content)        # Flipkart is the Online shopping, Amazon is the best online shopping
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


# def skip_first_line(file_name):
#     """Skips the first line of a text file."""
#     with open(file_name, "r") as f:
#         next(f)
#
#
# if __name__ == "__main__":
#     skip_first_line("myfile.txt")

# odd = True
#
# with open('file.txt') as f:
#     for line in f:
#         if odd:
#             print(line, end='')
#         odd = not odd

with open('data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line != '':
            # process a line.
            print(line)
        else:
            pass #  skip line
