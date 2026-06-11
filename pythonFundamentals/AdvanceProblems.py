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

'''

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


