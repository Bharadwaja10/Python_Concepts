# l = eval(input()) "eval can take any type of data from the user"
# print(l)
# print(type(l))

"List"
# A list is an ordered collection of different datatypes, represented with square brackets [].
# Lists are mutable, meaning their elements can be changed after they are created.

l = [1, 2, 3, 4, 5, 6]

# Remove the value at the given index (index 0 in this case).
del(l[0])

# Removes the last element in the list.
l.pop()

# Removes the first occurrence of the given value (in this case, 4).
l.remove(4)

# Clears the list, removing all elements.
l.clear()

print(l)  # Output: []

# Re-initialize the list for further operations.
l = [1, 2, 3, 4, 5, 6]

# Count how many times the value 1 appears in the list.
print(l.count(1))  # Output: 1

# Returns the length (number of elements) in the list.
print(len(l))  # Output: 6

# Returns the index of the first occurrence of the value 2.
print(l.index(2))  # Output: 1

# Insert a value at the given index without removing the previous value.
l.insert(1, 10)

# Append a value to the end of the list.
a = [10, 20]
l.append(a)  # Appends the list a as a single element.
l.append(7)  # Appends 7 to the list.

print(l)  # Output: [1, 10, 2, 3, 4, 5, 6, [10, 20], 7]

# Extend the list by adding each element from another iterable (e.g., list a).
l.extend(a)

print(l)  # Output: [1, 10, 2, 3, 4, 5, 6, [10, 20], 7, 10, 20]

"List Comprehension"
# It is an elegant way to create a list using a single line of code.
l1 = [i * 10 for i in range(1, 7)]
print(l1)  # Output: [10, 20, 30, 40, 50, 60]

"enumerate"
# The enumerate function is used to iterate over the list, providing both the index and value of each element.

l = [1, 2, 3, 4, 5, 6]
for index, value in enumerate(l):
    print(index, value)

# Output:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6

# The zip function is used to iterate over two lists simultaneously.

l1 = [10, 20, 30, 40, 50]
for i, j in zip(l, l1):
    print(i, j)

# Output:
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50

# Basic list functions:
print(sum(l))  # Output: Sum of the elements in the list -> 21
print(max(l))  # Output: Maximum value in the list -> 6
print(min(l))  # Output: Minimum value in the list -> 1

# Sort the list in ascending order.
l.sort()

# Reverse the list.
l.reverse()

print(l)  # Output after sort and reverse: [6, 5, 4, 3, 2, 1]



