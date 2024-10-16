# A Decorator is a function that takes another function as an argument,
# extends its functionalities, and returns the modified function
# without altering the original function code.
# Decorators are applied using the @ symbol.

def greet(func):
    def inner_func():
        print("Hello")  # Adding extra functionality before the original function
        func()  # Calling the original function
        print("The decorator has successfully modified the function")  # Adding functionality after the original function
    return inner_func


@greet  # fx = greet(fx) - This applies the decorator to fx function
def fx():
    print("This is a function being modified")


fx()  # Calling fx() actually calls inner_func()

