# Tuple is similar to a list; it is a collection of heterogeneous data.
# Tuples are denoted by parentheses ().
# Tuples are immutable, meaning their values cannot be changed after they are created.

t = (1, 2, 3, 4, 5, 6, 2)  # A tuple with some repeated values

# Finding the maximum value in the tuple
print(max(t))  # Output: 6

# Finding the minimum value in the tuple
print(min(t))  # Output: 1

# Getting the length of the tuple
print(len(t))  # Output: 7

# Finding the sum of the elements in the tuple
print(sum(t))  # Output: 23

# Getting the index of the first occurrence of the value 2
print(t.index(2))  # Output: 1

# Counting how many times the value 2 appears in the tuple
print(t.count(2))  # Output: 2
