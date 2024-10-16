# Class is a blueprint of the object. It contains methods and instance variables inside it.
# Object is a real-world entity or an instance of the class.
# When we create a class, no memory is allocated, but when we create an object, memory is allocated.
# Methods are actions or behaviors of the class.
# 'self' refers to the current instance of the class.

class Test:
    def dis(self):
        print("This is a dis method of the class Test")

    def empty(self):
        # We use the 'pass' keyword when we want to define an empty method, class, or function and avoid errors.
        pass


# Creating the object of the class
a = Test()

# Calling the method of the class Test
a.dis()


# Types Of Variables
# Object level variable: A variable declared inside a method of the class using 'self'.
# It is specific to an object.

# Class level variable: A variable declared outside any method but inside the class.
# It is accessed using the class name.

# Local variable: A variable declared inside a method and can be accessed only within that method.

class Test_1:
    # Class level variable
    a = 20

    def display(self):
        # Object level variable
        self.b = 30
        # Called by referring to the class name
        print("The class level variable is", Test_1.a)
        # Called by referring to the object of the class
        print("The object level variable is", self.b)

    def display_1(self):
        # Local variable
        c = 20
        print("The local level variable is", c)


# Creating an object and calling methods
t = Test_1()
t.display()
t.display_1()

# Accessing class level variable directly from the class
print(Test_1.a)


# Types Of Methods
# Object level method: A method that takes 'self' as a parameter and is dependent on the object of the class.

# Class level method: A method that takes 'cls' as a parameter and modifies class level variables.
# It uses the @classmethod decorator.

# Static method: A method that is independent of the object and does not modify class or instance variables.
# It uses the @staticmethod decorator.

class Test_2:
    company = "Apple"  # Class level variable

    # Constructor: Called automatically when an object is created. It is used to initialize instance variables.
    def __init__(self, name):
        self.name = name  # Instance variable

    def show(self):
        print(f"{self.name} is working in {self.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def static():
        a = 10
        b = 20
        print("Static method:", a + b)


# Object creation and method calls
t1 = Test_2("Alex")
t1.show()

# Changing the class level variable using a class method
t1.change_company("Tesla")
t1.show()

# Calling static method
t1.static()

# Changing class level variable again using the class method directly via class
Test_2.change_company("Google")
t1.show()

# Calling static method directly via class
Test_2.static()

'''class level variable and class level method and static level method are independent of the object of the class
 and object level method,variable are dependent of the object of the class local variable are only accessed inside
  the method only'''

# Example for parameterized constructor
class Test_3:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def dis(self):
        print("The parametrized values are ",self.a,self.b)

# initializing the values
t2=Test_3(10,30)
t2.dis()  # Output:The parametrized values are  10 30









