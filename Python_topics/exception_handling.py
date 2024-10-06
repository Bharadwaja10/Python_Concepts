# Exception handling is used to manage runtime errors.
# Runtime errors can include ZeroDivisionError, while compile-time errors include syntax errors.
# We use try, except, and finally blocks to handle exceptions.
# The try block is used to test a block of code for errors.
# If an error occurs, the execution stops and goes to the except block.
# The except block is used to handle the exceptions that occur in the try block.
# The finally block will execute regardless of whether an exception occurred or not.

def func():
    a = 10
    b = 0
    try:
        c = a / b  # This will raise a ZeroDivisionError
        c = c + 100

    except ZeroDivisionError:
        print("Denominator cannot be zero")

    # The default except block should be placed at the end of all except blocks
    except Exception as e:
        print("An error occurred: " + str(e))

    finally:
        print("Execution of the try-except block is complete.")


# Call the function
func()

