# Solve using If statements
# Question 1
#  Write a program that asks for a number and prints wheather it is positive, negative or zero
'''
num = int(input('Enter a number:'))
if num > 0:
    print('the number', num ," is Positive")
elif num<0:
    print('the number', num ," is Negative")
else:
    print('the number is zero')
# Question 2
# Create a program if a person is eligible to vote 

age = int(input('Enter your age: '))

if age>18:
    print('you are eligible to vote')
else:
    print('you are not eligible to vote. Sorry!')

# Question 3
# Write a program that take a number from the user and prints Even if its even otherwise Odd

num = int(input('Enter a number to check Even or Odd: '))
if num % 2 == 0: 
    print('It is Even number')
else:
    print('It is Odd number')

# Solve using Match Statements
# Question 4
# Ask user to enter a day number (1-7) and print the corresponding day 

num = int(input('enter a number between 1 to 7:'))

match num:
    case 1:
        print('day 1: Mon')
    case 2:
        print('day 2: Tue')
    case 3:
        print('day 3: wed')
    case 4:
        print('day 4: Thu')
    case 5:
        print('day 5: Fri')
    case 6:
        print('day 6: Sat')
    case 7:
        print('day 7: Sun')
    case _:
        print('Enter a vaild number')

# Question 5
# Write a program with match case to simulate a simple calculator 
# ask for 2 numbers and operator
# perform the operations using the match case.
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation=input('Enter the operation to perform eg. add, sub, mul, div : ')
match operation:
    case 'add':
        print('Add : ', num1 + num2)
    case 'sub':
        print('Sub : ', num1 - num2)
    case 'mul':
        print('Mul : ', num1 * num2)
    case 'div':
        print('Div : ', num1 / num2)

# Question 6
# Print numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)

# Question 7
# Print the multiplication table of a number (entered by user)
num= int(input('Enter the number for multiplication table: '))
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")

# Question 8
# Calculate the sum of all numbers from 1 to 100 using for loop
sum= 0
for i in range(1, 101):
    sum += i
print(f"the sum of 1 to 100 is {sum}")

# Question 9
# Print the patten using for loop
#*
#**
#***
#****
for i in range(1, 5):
    print('*'* i)

# While loop
# Question 10
# Print the number from 1 to 10 using while loop
i=1
while i<11:
    print(i)
    i +=1

# Question 11
# Write a program to keep asking the user to enter the correct password
password= 'tom'
while True:
    pwd=input('Enter the password: ')
    if password == pwd:
        break


# Question 12
# using a while loop reverse the given number
num= int(input('Enter the number to be reversed: '))
reverse=0
while num>0:
    getLastDigit = num %10
    reverse= reverse * 10 + getLastDigit
    num= num // 10
print(f"The reversed number is {reverse}")

# Question 13
# use a for loop to print numbers from 1 to 10 but stop the loop if the number is (use break)

for x in range(1, 11):
    if x==7:
        break
    print(x)


# Question 14
# Print number from 1 to 10 skipping the number 5 (use continue)

for x in range(1, 11):
    if x==5:
        continue
    print(x)


# Quesition 15
# write a loop that goes through numbers 1 to 5 but does nothing for number 3 (use pass)
for x in range(1, 6):
    match x:
        case 1:
            print('1')
        case 2:
            print('2')
        case 3:
            pass
        case 4:
            print('4')
        case 5:
            print('5')

# Question 16
# Write the fibonacci series using recursive function 

def fib(n):
    if n == 0 or n==1:
        return n
    return fib(n-2) + fib(n-1)

print(fib(6))


# Question 17
# create a funciton that greet that prints hello python learner when called
def greet():
    print('Hello Python Learner!')
greet()


# Question 18
# write a function square(num) that returnes the square of the given number. Test it with different numbers

def square(num):
    return num ** 2
squ = square(7)
print(squ)

# Question 19
# write a function fullname(firstname, lastname) that takes firstname and lastname as parameters and returns single string in the format 'first last'

def fullname(firstname, lastname):
    fullName= firstname + ' '+ lastname
    return fullName
print(fullname('mohammed','yousuf'))

# Question 20
# Write a function calArea(length, width=10) that returns the area of the rectangle. Test it by calling a function with both the length and width, only using length (with defaul width)

def calArea(length, width=10):
    return length * width
print(calArea(50, 100))
print(calArea(70))

# Question 21
# Write a lamda function that add two numbers and test it

add = lambda a , b: a + b
print(add(3,6))


# Question 22
# create a list= [1,2,3,4,5] and use map() to get their squares

list1 = [1,2,3,4,5]
square= lambda x: x*x
print(list(map(square, list1)))


# Question 23
# write a recursive function factorial(n) that returns the factorial of the number

def factorial(n):
    if n==1 or n== 0:
        return 1
    return factorial(n-1) * n
    
print(factorial(0))

'''

# Quesion 24
# write a recursive funciton sum of digits that returns the sum of all the digits of the given number

def sumOfDigits(n):
    if n==0:
        return 0
    return n%10 + sumOfDigits(n//10)
print(sumOfDigits(1234))