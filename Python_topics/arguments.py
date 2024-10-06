# func(a=10) is a function where 'a' is a parameter and 10 is an argument.

def func():
    print("This is a normal function")

# Parameterized function
def parameterized_func(a, b):
    print("The values of (a, b) are", a, "and", b)

def default_arg(a="This is a default value"):
    print(a)

def show(*args):
    print(args)

def show_1(**kwargs):
    print(kwargs["name"])

func()
# Calling parameterized function

# Positional arguments are passed in the same order as the parameters
parameterized_func(10, 20)

# Keyword arguments are passed with their parameter names
parameterized_func(a=10, b=20)  # Output: The values of (a, b) are 10 and 20
# parameterized_func(b=20, a=10)  # Output: The values of (a, b) are 10 and 20

# Default arguments are initialized when the function is defined
default_arg()  # Output: This is a default value
default_arg("This is a string")  # Output: This is a string

# Variable Length Arguments
# Arbitrary arguments (*args) allow us to pass any number of arguments.
# These arguments are captured as a tuple.
show(10, 20, 30, "this is a string")

# Arbitrary keyword arguments (**kwargs) allow us to pass any number of keyword arguments.
# These arguments are captured as a dictionary.
show_1(name="Rajesh", Class=10)
