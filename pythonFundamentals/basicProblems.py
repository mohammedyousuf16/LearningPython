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
'''

# Question 3
# Write a program that take a number from the user and prints Even if its even otherwise Odd

num = int(input('Enter a number to check Even or Odd: '))
if num % 2 == 0: 
    print('It is Even number')
else:
    print('It is Odd number')