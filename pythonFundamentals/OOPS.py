'''
class Employee:
   company = "HP"

   def get_salary(self):
    return 34000
e = Employee() # An Object of class Employee is created here print(e.get_salary()) # Employee e's get salary method is calle
print(e.get_salary()) # output: 34000

e2 = Employee()
print(e2.get_salary())

#Constructor in Python
class Employee:
   def __init__(self,slary, name, bond):
     self.salary = slary
     self.name = name   
     self.bond = bond

   def get_salary(self):
    return self.salary
   
   def get_Info(self):
     print(f'Employee name is {self.name} and his salary is {self.salary} and his bond is {self.bond} years')
     

e1 = Employee(32000, 'John', 5)
print(e1.get_salary())
e1.get_Info()


# instance and class attribute

class Employee:
   company = 'Asus'
   def __init__(self,slary, name, bond, company):
     self.salary = slary
     self.name = name   
     self.bond = bond
     self.company= company

   def get_salary(self):
    return self.salary
   
   def get_Info(self):
     print(f'Employee name is {self.name} and his salary is {self.salary} and his bond is {self.bond} years')  

e1= Employee(23000, 'john', 3, 'microsoft')
print(e1.company) # will always print instance attribute
print(Employee.company)

#Object introspection
print(dir(e1))


# Inheritance and Polymorphism

class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now....")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("Woof!")

a = Animal("Dog")
a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)


# Method Overriding and operator overloading

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2
p = p1 + p2 # We overloaded the + Operator by writing __add__ function
p.print_point() 

'''

#Decorators in python

# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# f = decorator(say_hello)
# f()
#     f will look something like this
# def f():
#     print("I am about to execute a function....")
#     print("Hello!")
#     print("I have executed this function....")


