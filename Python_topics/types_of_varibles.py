# Global Variable
# The scope of the global variable is all over the file
# We can access the global variable anywhere inside the file
a = 6

def func():
    # Local Variable
    # The scope of the variable is only inside the function
    b = 20
    print(a)  # Accessing global variable
    print(b)  # Local variable

# We use the global keyword to modify the global variable inside the function
def func_2():
    global a  # Declaring that we are modifying the global variable 'a'
    a = a - 1  # Modifying the global variable


if __name__ == "__main__":
    func()

    func_2()
    print(a)  # Output:5

    func_2()
    print(a)  # Output:4






