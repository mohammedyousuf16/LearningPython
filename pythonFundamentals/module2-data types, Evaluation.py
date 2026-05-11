# More about operators
print(2 + 3)  
print(5 - 2)
print(+12) #output: 12
print(-5) #output: -5

2 ** 2 ** 3 #exponentiation is evaluated from right to left, so this is equivalent to 2 ** (2 ** 3) which is 2 ** 8 = 256
print(2 ** 2 ** 3) #output: 256

# more about print and strings

len("Hello") #output: 5

print('Hello world') 
print ('learn python')

print('Hello world', end='.') 
print ('learn python')

first_name = 'John'
print('your first name is', first_name, 'Welcome to Python!') #output: your first name is John Welcome to Python!
print('your first name is', first_name, 'Welcome to Python!', sep='-') #output: your first name is-John-Welcome to Python!

# bitwise operators
print(5 & 3) #output: 1
print(5 | 3) #output: 7
print(5 ^ 3) #output: 6
print(~5)    #output: -6
print(5 << 1) #output: 10
print(5 >> 1) #output: 2

#if statements
user_age= int(input("Please enter your age: "))
if user_age > 30:
    print("You are over 30 years old.")
    print('you are not eligible for this offer')
elif user_age == 30:
    print('you are exactly 30 years old.')
    print('you are eligible for a better offer')
else:
    print('you are below 30 years old.')
    print('you are eligible for this offer')    

# Logical operators and condition
#
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# == equal to
# != not equal to

password = input("Enter your password: ")
if password != '--secret':
    print ('not correct password')
else:
    print('correct password')

if 2==2:
    print('true')
if 1==2:
    print('true')
if 2 == 2.0:
    print('true')

# joining multiple conditions

# using of and operator
user_age = int(input("Please enter your age: "))
user_country = input("Please enter your country: ")
if user_age <25 and user_country == 'USA':
    print('you are eligible for student discount')
else:
    print('you are not eligible for this offer')

# using of or operator
user_country = input("Please enter your country: ")
if user_country == 'USA' or user_country == 'Canada' or user_country == 'UK':
    print('you are eligible for this offer')
else:
    print('you are not eligible for this offer')

#using of not operator
user_country = input("Please enter your country: ")
if not user_country == 'Germany':
    print('you are not from Germany')
else:
    print('you are from Germany')

#using all three and or not operators together

user_age = int(input("Please enter your age: "))    
user_country = input("Please enter your country: ")     

if not user_country == 'Germany' and user_age < 25 or user_country == 'USA' and user_age > 30:
    print('you qualify')
else: 
    print('you do not qualify')

# Nested if statements
answer_a = input('do you like travelling y/n?')
if answer_a == 'y':
    answer_b= input('do you like Asia y/n?')
    if answer_b == 'y':
        print('excellent you can win ticket to thailand')
    else:
        print('sorry to hear that you don\'t like Asia')
else: 
    print('sorry to hear that')

# Exercise 4

purchasedBefore = int(input('How many days ago have you purchased the item? ')) 
itemUsed = input('Have you used the item at all [y/n]?  ')
brokenDown = input('Has the item broken down on its own [y/n]? ')

if purchasedBefore < 10 and itemUsed == 'n':
    print('you are eligible for the refund')
elif brokenDown == 'y':
    print('you are eligible for the refund')
else:
    print('u r not')

# while loop
