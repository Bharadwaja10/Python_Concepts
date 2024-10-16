# Polymorphism means getting different behaviors or outputs for the same action or function.
# It is a core concept of OOPs that allows a function or method to operate on objects of different types.
# Eg: Method overloading, method overriding, and duck typing.
# Note: Python does not support method overloading in the traditional sense (like in Java),
# but we can achieve similar behavior.

# Polymorphism with a function
# The same function 'add' can behave differently based on the types of the arguments passed to it.
def add(a, b):
    return a + b


print(add(3, 5))  # Output: 8 (integer addition)
print(add("Hello, ", "World!"))  # Output: Hello, World! (string concatenation)

# The 'add' function shows polymorphism as it can handle both integer addition and string concatenation
# based on the type of its arguments (int and str), which demonstrates polymorphism.

# METHOD OVERRIDING:
# Method overriding occurs when a child class provides a specific implementation of a method
# that is already defined in its parent class. The child class method will override the parent's method.


class Animal:
    def sound(self):
        print("This animal makes a sound")


class Dog(Animal):
    # The 'sound' method in the Dog class overrides the 'sound' method in the Animal class.
    def sound(self):
        print("The dog barks")


class Cat(Animal):
    # The 'sound' method in the Cat class also overrides the parent's 'sound' method.
    def sound(self):
        print("The cat meows")


# Creating instances
dog = Dog()
cat = Cat()

dog.sound()  # Output: The dog barks
cat.sound()  # Output: The cat meows

# Method overriding allows us to redefine the inherited method to suit the subclass's needs.

# METHOD OVERLOADING:
# Python does not natively support method overloading (same method name with different parameters).
# However, we can achieve similar behavior by setting default arguments and using conditional logic.


class Calculator:
    # The 'add' method handles different numbers of arguments using default 'None' values.
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c  # If three arguments are provided, sum all three.
        elif a is not None and b is not None:
            return a + b  # If only two arguments, sum them.
        else:
            return "Not enough arguments"  # If fewer than two arguments, return an error message.


calc = Calculator()
print(calc.add(2, 3))      # Output: 5 (sum of two numbers)
print(calc.add(2, 3, 4))   # Output: 9 (sum of three numbers)


# Although Python doesn't have method overloading directly, we can simulate it by setting default values and using conditions.

# DUCK TYPING:
# Duck typing is a concept in Python where the actual type of an object is not as important as the methods it defines.
# "If it looks like a duck and quacks like a duck, it's a duck."
# In duck typing, an object's behavior (methods it can execute) is more important than its type.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Duck:
    def sound(self):
        print("Quack")


# The 'make_sound' function does not care about the object's type, only that it has a 'sound' method.
def make_sound(animal):
    animal.sound()


# All these objects can call sound() method due to duck typing
dog = Dog()
cat = Cat()
duck = Duck()

make_sound(dog)   # Output: Bark
make_sound(cat)   # Output: Meow
make_sound(duck)  # Output: Quack

# In this example, all three objects (dog, cat, and duck) have the same method signature (sound()),
# so the make_sound function can call the method regardless of the object's type.

# OPERATOR OVERLOADING:
# In Python, operator overloading allows us to define the behavior of operators (like +, -, *, etc.)
# for custom objects by overriding special methods (also known as magic methods).
# Example: Overloading the + operator using the '__add__' method.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator to add two Point objects.
    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    # Overloading the __str__ method for a more readable output when printing Point objects.
    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Creating two Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Adding two points using the overloaded + operator
result = point1 + point2

print(result)  # Output: Point(6, 8)

# In this example, we have overloaded the + operator to work with Point objects.
# When we add two Point objects (point1 and point2), the __add__ method is called to combine their coordinates.

# This will run the __str__ method
print(point1)
