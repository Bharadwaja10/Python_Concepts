# File handling is essential for programmers to manage files effectively.
# This includes creating, reading, writing, and appending data to files.

# Open a file for writing ('w' mode)
f = open("sample.txt", "w")

# This will create the sample file if it does not exist and write the specified text to the file.
# If the text is already present in the file, it will be overridden.
f.write("This is the sample file.")
f.close()  # Close the file after writing.

# Open the file for appending ('a' mode)
f = open("sample.txt", "a")

# The write() method is used to append text at the end of the file without overriding existing content.
f.write("\nit is a next line.")  # Use write() instead of append().
f.close()  # Close the file after appending.

# Open the file for reading ('r' mode)
f = open("sample.txt", "r")

# The tell() method returns the current position of the cursor in the file.
print(f.tell())  # Output: 0 (cursor is at the start)

# The seek() method moves the cursor to a specified index.
print(f.seek(5))  # Move the cursor to index 5 (it returns the new cursor position).

# Read the entire content of the file.
print(f.read())  # Output the content of the file from the current cursor position.

# Read a single line from the current cursor position.
print(f.readline())  # Output the next line from the cursor position.

# Read all remaining lines from the current cursor position and return them as a list.
print(f.readlines())  # Output all remaining lines as a list.

f.close()  # Close the file after reading.
