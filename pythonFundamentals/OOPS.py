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

'''

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