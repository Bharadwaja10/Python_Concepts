# Recursion is when a function calls itself
def fact(n):
    if n == 1 or n == 0:  # Base case
        return 1  # Factorial of 0 or 1 is 1
    else:
        return n * fact(n - 1)  # Recursive call reducing n by 1


print(fact(6))

# Anonymous functions are the nameless functions such as lambda function
# Lambda functions are the functions which can has any no of variables but has only one expression
# syntax: lambda argument_list:expression
s = lambda a, b, c: a + b + c
print(s(10, 20, 30))

# filter() is used when we filter the values from the given iterable
# It takes function and iterable as an arguments
l = [1, 2, 3, 4]
even = list(filter(lambda a: a % 2 == 0, l))
print(even)  # Output:[2, 4]

# map() is used to generate a new elements by doing some operation for every element in the iterable
new = list(map((lambda a: a * 2), l))
print(new)  # Output:[2, 4, 6, 8]

# reduce() is used to reduce the sequence of elements in to single value
# We need to import functools to work with it
from functools import *

value = reduce(lambda a, b: a + b, l)
print(value)  # Output:10
