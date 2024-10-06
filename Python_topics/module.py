# module is a python file which can be imported and used the python file classes and functionalities
# Importing the math module for mathematical functions
import math

# Using the sqrt function to calculate the square root of 25
print("Square root of 25:", math.sqrt(25))  # Output: 5.0

# Using ceil function to round up to the nearest integer
print("Ceiling of 4.2:", math.ceil(4.2))  # Output: 5

# Using floor function to round down to the nearest integer
print("Floor of 4.7:", math.floor(4.7))  # Output: 4

# Using fabs function to get the absolute value of a number
print("Absolute value of -5.5:", math.fabs(-5.5))  # Output: 5.5

# Importing the random module for generating random numbers
import random

# Using random to get a random float between 0.0 and 1.0
print("Random float between 0 and 1:", random.random())

# Using randint to get a random integer between two inclusive values
print("Random integer between 1 and 10:", random.randint(1, 10))  # Output:  Selects a random integer between 1 and  10, inclusive.

# Using randrange to get a random integer within a specified range
print("Random integer from range 1 to 10:", random.randrange(1, 10))  # Output: Generates a random integer between 1 and 9 (10 is exclusive)

# Using uniform to get a random float within a specified range
print("Random float between 1 and 10:", random.uniform(1, 10))  # Output: Random float in the range

# Using choice to select a random element from a list
my_list = ['apple', 'banana', 'cherry', 'date']
print("Random choice from list:", random.choice(my_list))  # Output: Random fruit from the list

