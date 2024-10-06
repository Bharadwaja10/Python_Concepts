import pickle

# The pickle module is used to serialize and deserialize Python objects.
# Serialization converts a Python object into byte code,
# while deserialization converts the byte code back into a Python object.
# Here we write and read the file by "wb","rb"

# Example list to be serialized
l = [10, 20, 30, 40]

# Open a file for writing in binary mode ('wb')
f = open("sample2.txt", "wb")

# dump() method takes two parameters: the object to be serialized and the file object.
# It will serialize the object and write it to the file.
pickle.dump(l, f)

# dumps() method takes only one parameter: the Python object.
# It will serialize the object and return the byte code.
a = pickle.dumps(l)
print(a)  # Output: byte representation of the list

f.close()  # Close the file after writing.

# Open the file for reading in binary mode ('rb')
f = open("sample2.txt", "rb")

# load() method reads the serialized object from the file and deserializes it.
read = pickle.load(f)
print(read)  # Output: [10, 20, 30, 40]

# loads() method takes a byte code as an argument and deserializes it.
# Example of using loads() with byte code.
r = pickle.loads(a)  # Deserializing using the byte code from the dumps()
print(r)  # Output: [10, 20, 30, 40]

f.close()  # Close the file after reading.






