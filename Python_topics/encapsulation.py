# Encapsulation means binding of data (attributes) and methods (functions) together into a
# single unit (class).
# It restricts direct access to the internal variables of a class to ensure data security.
# We use access specifiers to control how data can be accessed from outside the class.
# There are three types of access specifiers in Python:
# 1. **Public**: Variables and methods declared without any leading underscore are public by default.
#    They can be accessed from both inside and outside the class.
# 2. **Protected**: Variables and methods with a single leading underscore (_) are considered protected.
#    By convention, these should not be accessed outside the class, except by subclasses (inherited classes).
# 3. **Private**: Variables and methods with a double leading underscore (__) are private.
#    They can only be accessed from within the class itself.

class Test:
    # Public variable
    a = 10

    # Protected variable
    _b = 20

    # Private variable
    __c = 30

    # Public method to access the variables
    def get(self):
        print("a :", self.a)  # Public attribute
        print("_b : ", self._b)  # Protected attribute
        print("__C : ", self.__c)  # Private attribute

    # Setter method to modify the private attribute __c
    def set(self, c):
        self.__c = c  # This method allows modification of the private attribute


# Creating an object of the Test class
t = Test()

# Accessing the public variable directly
print(t.a)  # Output: 10 (public variables can be accessed directly)

# Accessing the protected variable directly
print(t._b)  # Output: 20 (although protected, Python allows access outside the class by convention)

# Trying to access the private variable directly
# print(t.__c)  # This will raise an AttributeError because __c is private and can't be accessed directly

# Accessing the private variable using the getter method
t.get()  # This will output the value of __c because it's accessed inside the class

# Modifying the private variable __c using the setter method
t.set(10)

# Accessing the updated private variable through the getter method
t.get()  # Now __c has been modified to 10

# Using dir() to see all attributes and methods, including the "mangled" private attribute names.
print(dir(t))

# Python name mangling: Private attributes are internally renamed to include the class name.
# The private attribute __c is renamed as _Test__c internally.
# We can access it using the mangled name (not recommended as it breaks encapsulation).
print(t._Test__c)  # Output: 10 (this is how private variables can be accessed, though not encouraged)



