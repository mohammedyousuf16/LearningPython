# Dunder/Magic methods
'''
class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)


e = Employee("Harry", 43566)
print(len(e))
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))

#Exception handeling and custom Errors


while False:
    try: 
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The division is {a / b}")

    except ValueError:
        print("Please dont perform bad typecasts")
    
    except ZeroDivisionError:
        print("Hey dont divide by 0")

    except Exception as e:
        print("Unknown error occurred!", e)

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please dont divide by 0")

print(f"The division is {a / b}")


# Else
try:
    a = 345/10

except Exception as e:
    print(e)

# Gets executed when there is no error in the try block 
else:
    print("Hey I am good")

# Finally

def divide(a, b):
    try:
        c = a/b 
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

    # This is always executed no matter if try completely executes or not 
    finally: 
        print("This is always executed")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
divide(a, b)

#---Map---

numbers = [1, 2, 3, 45, 4, 21]

# def square(x):
#     return x * x 


new = list(map(lambda x: x*x, numbers))
print(new)


#---Filter---

# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a = [1, 3, 5, 234, 34, 32, 6543, 23, 2 ,5 , 6, 7 ,43]

new = list(filter(lambda x: x>9, a))
print(new)

#---Reduce---

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
#         [3, 3, 4, 5, 6]
#         [6, 4, 5, 6]
#         [10, 5, 6]
#         [15, 6]
#         [21]

def sum(a, b):
    return a + b 

c = reduce(sum, numbers)
print(c)


#Walrus Operator

def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

# # a = very_slow_func()
# if((a:=very_slow_func())>10):
#     print(a)

# else:
#     print("Its not greater than 10")

while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break 


# Args 

def sum(*args):
    total=0
    for item in args:
        total+= item
    return total

print(sum(3,23,5,56,67,5))


#Kwargs

def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks 
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, vikrant=54, jack=34, Marie=90, Priya=45)

'''

# Args and Kwargs togeather

def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=34, jill=32, marie=31)


