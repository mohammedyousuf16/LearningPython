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