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

'''
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