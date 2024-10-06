# A Generator is a function that contains the 'yield' keyword.
# Instead of returning a single value, it returns a sequence of values one at a time as an iterator.
# Each time 'yield' is encountered, the function's state is saved, and it resumes where it left off when called again.

def display():
    yield 19
    yield 20
    yield 21

# Creating a generator object
d = display()

# Using 'next()' to retrieve the next value from the generator
print(next(d))  # Output: 19
print(next(d))  # Output: 20
