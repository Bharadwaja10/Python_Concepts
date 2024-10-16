# Inheritance means taking the properties and methods of one class into another class.

# Example of Multi-level Inheritance
class Iphone1:
    def display(self):
        print("This is a 5 inches display")

    def camera(self):
        print("Camera is 15 megapixels")


class Iphone2(Iphone1):
    # Method overriding: the Parent class's method and Child class have same method name
    # def display(self):
    #     super().display() #It is used to call the parent class method from the child class
    #     print("This is a 7 inches display")

    def bluetooth(self):
        print("Bluetooth is available to share songs")


class Iphone3(Iphone2):
    def charger(self):
        print("The charger is 20 watts")


# Creating an object of Iphone3, which inherits from Iphone1 and Iphone2
iphone_obj = Iphone3()
iphone_obj.display()  # Inherited from Iphone1 (or overridden by Iphone2 if uncommented)
iphone_obj.camera()  # Inherited from Iphone1
iphone_obj.bluetooth()  # Inherited from Iphone2
iphone_obj.charger()  # Defined in Iphone3


# Example of Multiple Inheritance
class Parent1:
    def greet(self):
        print("Hello from Parent1")


class Parent2:
    def greet(self):
        print("Hello from Parent2")


# Child class inheriting from both Parent1 and Parent2
class Child(Parent1, Parent2):
    pass


# Creating an object of the Child class
child_obj = Child()

# Calling the greet method
child_obj.greet()  # Output: Hello from Parent1 (since Parent1 is the first inherited class)
