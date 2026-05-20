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
'''
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
