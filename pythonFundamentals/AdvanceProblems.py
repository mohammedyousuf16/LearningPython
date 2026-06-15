'''
# Question 1
# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!" .

def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@logger
def say_hello():
    print('Hello!')

say_hello()


# Question 2

# Write a decorator timer that calculates how long a function takes to execute.
# Test it with a function that sums numbers from 1 to 1,000,000.

from time import time

def timer(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2=time()
        time_taken=f' Time taken to calculate {t2-t1}'
        return time_taken
    return wrapper

@timer
def sum(n):
    total= 0
    for i in range(1, n+1):
        total += i
    print(f'sum on {n} is {total}')
print(sum(1000000))


# Question 3

# Create a class Employee with a private attribute _salary .
# Use @property to define a getter for salary .
# Use @salary.setter to prevent setting negative values (print a warning
# instead).
# Create an object and test by setting positive and negative salaries.

class Employee:

    def __init__(self, salary):
        self.__salary= salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, newsalray):
        if(newsalray>0):
            self.__salary= newsalray
        else:
            print('salary cant be in negative')

e1= Employee(3000)
print(e1.salary)# output 3000
e1.salary=-5000 # output salary cant be in negative
print(e1.salary)# output 3000
e1.salary=5000 # output "sets the __salary to 5000"
print(e1.salary)# output 5000


# Question 4 
# Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b .
# A @classmethod called description(cls) that prints "This is a utility class for math operations."
# Call both methods without creating an object

class MathUtils:
    def __init__(self):
        pass

    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        return "This is a utility class for math operations."

print(MathUtils.add(2,4))
print(MathUtils.description())


# Question 5

# Create a class Book with attributes title and author .
# Implement __str__() so that printing the object displays "Title by
# Author" .
# Implement __len__() so that len(book) returns the length of the title.
# Create two Book objects and test these methods

class Book:
    def __init__(self, title, author):
        self.title= title
        self.author= author

    def __str__(self):
        return (f'{self.title} is an amazing book by {self.author} ')
    
    def __len__(self):
        return(len(self.title))

b1=Book('paris Adventure','john')
b2=Book('love in paris','Smith')
print(str(b1))
print(len(b1))
print(str(b2))
print(len(b2))

'''

# Question 6

# Write a program that asks the user to enter a number and handles:
# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
# Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

class NegativeNumberError(Exception):
    pass

try:
    num1= int(input('enter the number 1: '))
    num2= int(input('enter the number 2: '))
    
    if num1 < 0 or num2 <0:
        raise NegativeNumberError("Negative numbers are not allowed!")
        

    def divide(a,b):
        print(a/b)
    
    divide(num1, num2)
    
except ZeroDivisionError:
    print("can't didvide by the number zero")

except ValueError:
    print('please enter a valid number')

except NegativeNumberError as error:
    print(f'Invalid input: {error}')