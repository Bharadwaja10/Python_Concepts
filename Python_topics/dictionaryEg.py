# Dictionary is an unordered collection of key-value pairs enclosed in curly braces {}.
# A dictionary is a mutable datatype.
# In a dictionary, we can have duplicate values, but the keys must be unique.

# Example dictionary
dict_example = {"Course": "Python", "Duration": "2 Months", "Fees": 5000}
print(dict_example)

# Type of the dictionary
print(type(dict_example))  # Output: <class 'dict'>

"Keys in a dictionary are unique. If you try to add a duplicate key, it will overwrite the existing value for that key."
# dict={"Course":"python","Duration":"2 Months","Fees":5000,"Fees":90000}
# print(dict)  # Output: {'Course': 'python', 'Duration': '2 Months', 'Fees': 90000}

# keys
print(dict_example.keys())  # Gives all keys output:dict_keys(['Course', 'Duration', 'Fees'])
for i in dict_example.keys():
    print(i)
# Output:
# Course
# Duration
# Fees

# Values
print(dict_example.values())  # Output: dict_values(['python', '2 Months', 5000])
for i in dict_example.values():
    print(i)
# Output:
# python
# 2 Months
# 5000

# items
print(dict_example.items())  # Output:dict_items([('Course', 'python'), ('Duration', '2 Months'), ('Fees', 5000)])
for i in dict_example.items():
    print(i)
# Output:
# ('Course', 'python')
# ('Duration', '2 Months')
# ('Fees', 5000)

# pop() removes the item of the key passed
dict_example.pop("Fees")  # It will remove the item which has the key Fees

print(dict_example)  # Output:{'Course': 'Python', 'Duration': '2 Months'}

# get() will give the value of the given key
print(dict_example.get("Course"))  # Output:Python

# popitem() will remove the last item inserted in the dictionary
print(dict_example.popitem())  # Output:('Duration', '2 Months')

# dict() used to create a new dictionary
dict_new=dict(Course="Python",Duration='2 Months',Fees=5000)
print(dict_new)  # Output:{'Course': 'Python', 'Duration': '2 Months', 'Fees': 5000}

dict_new1=dict([('Course', 'Python'), ('Duration','2 Months'), ('Fees', 5000)])
print(dict_new1)  # Output:{'Course': 'Python', 'Duration': '2 Months', 'Fees': 5000}

dict_example = {"Course": "Python", "Duration": "2 Months", "Fees": 5000}

# update method is used to update the dictionary
dict_example.update({"Fees":9000})
print(dict_example)  # Output:{'Course': 'Python', 'Duration': '2 Months', 'Fees': 9000}






