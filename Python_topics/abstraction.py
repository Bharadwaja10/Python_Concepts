from abc import ABC, abstractmethod

# Abstraction refers to the concept of hiding the internal implementation details of an object
# and only exposing the essential features or functionalities.
# It allows us to define a blueprint for other classes to follow, enforcing a consistent interface.
# Abstraction is essential in security, modularity, and preventing the unnecessary exposure of functionality.

# In Python, abstraction is achieved using abstract classes and methods.
# Abstract classes cannot be instantiated directly and must be inherited by other classes.
# Abstract methods are methods declared in the abstract class but have no implementation,
# forcing the child classes to implement them.

# 'ABC' is the superclass for defining abstract classes in Python.
# 'abstractmethod' is a decorator that marks a method as abstract.

class Car(ABC):  # Car is an abstract class
    # Abstract method defined using @abstractmethod decorator
    # All classes inheriting Car must implement this method
    @abstractmethod
    def speed(self):
        pass  # This is just a placeholder, child classes will define the method

    # Concrete method, which is defined and can be inherited or overridden by child classes.
    def lights(self):
        print("There are lights")  # This is a common feature for all cars

# Child class Alto inherits from Car and must implement the abstract method 'speed'
class Alto(Car):
    # Implementing the abstract method
    def speed(self):
        print("max speed 150 kmph")  # This method is now defined in the child class Alto

    # New method specific to the Alto class
    def brakes(self):
        print("We have hydraulic brakes")  # Additional functionality for Alto

# Creating an instance of the child class Alto
t = Alto()

# Calling the implemented abstract method 'speed'
t.speed()  # Output: max speed 150 kmph

# Calling the method 'brakes' defined in Alto
t.brakes()  # Output: We have hydraulic brakes

# The 'lights' method is inherited from the parent class and can be called without being redefined.
t.lights()  # Output: There are lights
