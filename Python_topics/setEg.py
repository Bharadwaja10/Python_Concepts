# Set is an unordered collection of heterogeneous, unique data.
# Sets cannot contain duplicate values.
# The values of a set are placed inside curly braces {}.

s = {1, 2, 3, 4, 5, 6, 7, 2, 1}  # Duplicate values (2 and 1) are automatically removed.
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7}

# remove() removes a specific element from the set, raises KeyError if the element is not present.
s.remove(6)
print(s)  # Output: {1, 2, 3, 4, 5, 7}

# discard() removes an element from the set if present, does nothing if the element is not present (no error).
s.discard(8)
print(s)  # Output: {1, 2, 3, 4, 5, 7} (since 8 was not in the set)

# pop() removes and returns an arbitrary element from the set, since sets are unordered.
s.pop()
print(s)  # Output could be {2, 3, 4, 5, 7} (the removed element is arbitrary)

# add() inserts a single element into the set.
s.add(8)
print(s)  # Output: {2, 3, 4, 5, 7, 8}

# update() inserts elements from an iterable (e.g., list, set) into the set.
s.update([30, 50, 70])
print(s)  # Output: {2, 3, 4, 5, 7, 8, 30, 50, 70}

# Performing set operations:
s = {1, 2, 3}
l = {1, 4, 5, 6}

# union() returns a set containing all unique elements from both sets.
print(s.union(l))  # Output: {1, 2, 3, 4, 5, 6}

# intersection() returns a set containing only the elements present in both sets.
print(s.intersection(l))  # Output: {1}

# difference() returns the elements present in 's' but not in 'l'.
print(s.difference(l))  # Output: {2, 3}

# symmetric_difference() returns the elements that are in either of the sets but not in both.
print(s.symmetric_difference(l))  # Output: {2, 3, 4, 5, 6}


