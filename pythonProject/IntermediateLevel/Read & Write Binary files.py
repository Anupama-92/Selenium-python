# Reading Entire Binary File:
with open('binaryfile.bin', 'rb') as file:
    content = file.read()
    print(content)

# Reading Binary File in Chunks:
chunk_size = 1024
with open('binaryfile.bin', 'rb') as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        print(chunk)

# Writing Bytes to a Binary File:
with open('binaryfile.bin', 'wb') as file:
    file.write(b'\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64\x21')

# Appending Bytes to a Binary File:
with open('binaryfile.bin', 'ab') as file:
    file.write(b'\x0A\x41\x70\x70\x65\x6E\x64')

# Converting a text file into binary file
# Open the text file for reading
with open('textfile.txt', 'r') as text_file:
    text_content = text_file.read()

# Open a new binary file for writing
with open('binaryfile.bin', 'wb') as binary_file:
    # Convert the text content to bytes and write it to the binary file
    binary_file.write(text_content.encode('utf-8'))