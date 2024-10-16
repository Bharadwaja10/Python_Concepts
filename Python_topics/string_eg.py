# String is a collection of one or more characters enclosed in single (''), double (""), or triple (''' ''') quotes.
# Strings are immutable, meaning the object cannot change its state or content after it is created.

s = "Welcome"
str_example = "this is a string"

# Removes spaces from the beginning and the end of the string.
print(s.strip())

# Converts the string to uppercase.
print(s.upper())

# Converts the string to lowercase.
print(s.lower())

# Swaps the case: uppercase becomes lowercase, and lowercase becomes uppercase.
print(s.swapcase())

# Capitalizes the first letter of each word in the string.
print(str_example.title())

# Finds the first occurrence of the specified character.
print(s.find("e"))  # Output: 1

# Finds the first occurrence of the specified character, starting from index 2.
print(s.find("e", 2))  # Output: 6

# Returns -1 if the specified character is not found.
print(s.find("a"))  # Output: -1

# Same as find(), but raises an error if the character is not found.
print(s.index("l"))  # Output: 2

# Finds the first occurrence of 'e', starting from index 2.
print(s.index("e", 2))  # Output: 6

# Checks if all characters in the string are alphabetic.
print(s.isalpha())  # Output: True

# Checks if all characters in the string are digits.
print(s.isdigit())  # Output: False

# Checks if there are no special characters in the string.
print(s.isalnum())  # Output: True

# Checks if all characters are alphabetic (will return False because of spaces in the string).
print(str_example.isalpha())  # Output: False

# Counts how many times the specified character appears in the string.
print(s.count("e"))  # Output: 2

# Converts the ASCII code to the corresponding character.
print(chr(97))  # Output: a

# Converts the character 'A' into its ASCII code.
print(ord("A"))  # Output: 65

# Replaces the old substring with the new substring.
print(str_example.replace("this", "This"))  # Output: "This is a string"

# Converts the string into a list of words.
a = str_example.split()
print(a)  # Output: ['this', 'is', 'a', 'string']

# Converts a list back into a string.
a = " ".join(a)  # Adds a space as the separator between the elements.
print(a)  # Output: "this is a string"

"String Formatting"
# We can format a string using placeholders {} inside the string.
# Inside the placeholders, we can place Python expressions, and they will be replaced with their values.

# Using f-string formatting (available in Python 3.6+).
name = "Alice"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is Alice and I am 25 years old."

# Using the format() method.
formatted_string1 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string1)  # Output: "My name is Alice and I am 25 years old."


