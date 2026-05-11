print('hello world')

# by using \ you can skip the char 
print('I\'m lerarning python')
print('and having fun')

# 2 sentence in a single print function
print('I\'m lerarning python', 'and having fun')

# using \n to put sting into new line
print('I\'m lerarning\npython')

# Variables

greeting='Hello, friend!'
print(greeting)
#variables value change if you re-assign to a differnt value
greeting='Hi, everybody!'
print(greeting)

#_correctNameVariable
#correctNameVariable
#correctName89Variable
#89incorrectVariable

#Data types

greeting= 'Hello, Friend' # string
age=35 #int
speed1= 4.5 #float
speed2=4.0 #float
speed3=4. #float

am_i_ugly= True  #Boolean
am_i_ugly= False #Boolean


#Numarical Representations

12000300 #hard to read
12_000_300 #underscores in number (easy to read)

#scientific notations
#3E4= 3e4 = 3*10000 = 30000
# 3e-4 = 3E-4 = 3 * 1/10000 = 0.0003
print(0.000000000000000000000000003) #output = 3e-27

#octal numbers
#starts with 0o or 0O
print(0o123) #output = 83

#hexadecimal numbers
#starts with 0X or 0x
print(0x123) #output = 291

#Operators
print(2-3)
print(3+7)
print(2*3)

#standard division
print(6/2)
print(7/2)

#integer division
print(6//2)
print(7//2) # output = 3 will get the lowest whole number

#modulus division
print(6%2) #will give the reminder value as 0
print(7%2) #will give the reminder value as 1

#power operator
print(2**3) #output = 2*2*2 = 8

#adding int with float will get float

print(2+3.0) #output = 5.0

# exercise 1

income = 250_000
lowtaxland_rate=0.05
ripoffland_rate=0.43
lowtax_Amt= income * lowtaxland_rate
ripoff_Amt= income * ripoffland_rate
taxAmtDiff = ripoff_Amt - lowtax_Amt

print('Your income is 250000 and you would pay',lowtax_Amt ,'income tax in Lowtaxland or',ripoff_Amt,'income tax in Ripoffland. You would save',taxAmtDiff,'by paying taxes in Lowtaxland!')


#Reasinging Values

age=28
print(age)
newAge= age +5 
print(newAge) #output = 33

age =28
age= age + 7
print(age) #output = 35

age = 28
age += 7 
print(age) #output = 35
age *= 2
print(age) #output = 70
age /= 2
print(age) #output = 35.0
age -= 7
print(age) #output = 28.0

#string concatenation
firstName= 'John' + 'smith'
print(firstName) #output = Johnsmith

print(firstName*5) #output = JohnsmithJohnsmithJohnsmithJohnsmithJohnsmith

print('23' + '2') #output = 232

#input function

#name = input('What is your name? ')
#print('Hello,', name)
#or 
#print('What is your name? ')
#name = input()  
#print('Hello,', name)

#exercise 2
#login = input('Enter your login: ')
#language = input('Enter your native language: ')

#print('Your login is', login, 'and you speak', language)

#Type casting
height_cm= input('Enter your height in cm: ')
float_height_cm = float(height_cm) / 30.48
print('Your height in feet is', float_height_cm) #output = Your height in cm is 180
#or
height_cm= float(input('Enter your height in cm: '))
print('Your height in feet is', height_cm / 30.48) #output = Your height in cm is 180

year_born = int(input('Enter your year of birth: '))
print('in 2100, you will be', 2100 - year_born, 'years old') #output = Enter your year of birth: 1990

temp_c = input('Enter the temperature in Celsius: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement= str(temp_c) + ' degrees Celsius is equal to ' + str(temp_f) + ' degrees Fahrenheit.'
print(temp_statement)

#exercise 3
hours= input('How many hours did you work last month? ')
hourlyRate= input('What is your hourly rate? ')
earned= float(hours) * float(hourlyRate)
print('Last month, you earned', earned, 'dollars')