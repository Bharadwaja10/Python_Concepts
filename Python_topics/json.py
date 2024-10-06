import json

# JSON (JavaScript Object Notation) is a lightweight data interchange format.
# It is used to convert Python objects to JSON strings and vice versa.

# Example list to be serialized
l = [10, 20, 30, 40]

# Open a file for writing in text mode ('w') since JSON is a text format.
f = open("sample2.txt", "w")

# dump() method takes two parameters: the object to be serialized and the file object.
# It will serialize the object and write it to the file in JSON format.
json.dump(l, f)

# dumps() method takes one parameter: the Python object.
# It will serialize the object and return the JSON string.
a = json.dumps(l)
print(a)  # Output: JSON string representation of the list

f.close()  # Close the file after writing.

# Open the file for reading in text mode ('r') since JSON is a text format.
f = open("sample2.txt", "r")

# load() method reads the serialized JSON object from the file and deserializes it back to a Python object.
read = json.load(f)
print(read)  # Output: [10, 20, 30, 40]

# loads() method takes a JSON string as an argument and deserializes it into a Python object.
# Example of using loads() with the JSON string from dumps().
r = json.loads(a)  # Deserializing using the JSON string from dumps()
print(r)  # Output: [10, 20, 30, 40]

f.close()  # Close the file after reading.
