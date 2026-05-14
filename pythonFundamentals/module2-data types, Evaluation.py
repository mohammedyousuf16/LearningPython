'''# More about operators
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
counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('finished')

secretNumber = 14
print(''
-----------------------------------
--- Secret Number Guessing Game ---
-----------------------------------'')
userInput = int(input('guess the secret number between 1 and 20: '))
while userInput != secretNumber:
    print('wrong guess, try again')
    userInput =int(input('guess the secret number between 1 and 20: '))
print('congratualations, you guessed the secret number!')

# For loop
for letter in 'hello':
    print('current letter is:', letter)

for counter in range(1,11):
    print(counter) #output: 1 2 3 4 5 6 7 8 9 10

for counter in range (11):
    print(counter) #output: 0 1 2 3 4 5 6 7 8 9 10

for counter in range(1,11,2):
    print(counter) #output: 1 3 5 7 9

# Break and continue statements

while True:
    name = input('enter your name or EXIT to quit: ')
    if name == 'EXIT':
        break
    print('hello', name)


for i in range(1, 20):
    if i % 5 == 0:
        continue
    print (i) #output: 1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19

# loops additional

for i in range(11):
    pass # this is a placeholder for future code, it does nothing and allows the loop to run without any action

for a in range (1,6):
    for b in range(1,6):
        print(a, 'x' ,b, '=', a*b) # this will print the multiplication table from 1 to 5

i = 5
while i <5:
    print(i)
    i += 1
else:
    print(i) # else statement will executed even if the while loop is true

# Exercise 5

while True:
    userInput = int(input('Guess the year when python 1.0 was released:'))
    if userInput < 1994:
        print('It was later than that!')
    elif userInput > 1994:
        print('It was earlier than that!')
    else:
        print('correct')
        break
       

# introduction to lists

emptyList = []
top_cities = ['New York', 'London', 'Tokyo', 'Paris']
print(f"the top cities are: {top_cities[1]}") #output: the top cities are: London --> this is a string vlaue, not a list
print(f"the top cities are: {top_cities[-1]}") #output: the top cities are: Paris 
print(f"the top cities are: {top_cities[0:2]}") #output: the top cities are: ['New York', 'London'] --> if you use slicing, it will return a list, even if it contains only one element
print(f"the top cities are: {top_cities[2:]}") #output: the top cities are: ['Tokyo', 'Paris']
print(f"the top cities are: {top_cities[:3]}") #output: the top cities are: ['New York', 'London', 'Tokyo']]


# Deleting elements from a list

top_cities = ['New York', 'London', 'Tokyo', 'Paris']
del top_cities[2]
print(top_cities) #output: ['New York', 'London', 'Paris']
top_cities = ['New York', 'London', 'Tokyo', 'Paris']
del top_cities[1:3]
print(top_cities) #output: ['New York', 'Paris']
top_cities = ['New York', 'London', 'Tokyo', 'Paris']
del top_cities[:]
print(top_cities) #output: []
top_cities = ['New York', 'London', 'Tokyo', 'Paris']
del top_cities
print(top_cities) #output: NameError: name 'top_cities' is not defined --> this is because we have deleted the entire list


# add elements to a list
BookRatings = [5, 7, 8, 9, 10]
BookRatings.append(4) # this will add 4 to the end of the list
print(BookRatings) #output: [5, 7, 8, 9, 10, 4]
BookRatings.insert(2, 6) # this will insert 6 at index 2
print(BookRatings) #output: [5, 7, 6, 8, 9, 10, 4]
BookRatings.extend([3, 2]) # this will add 3 and 2 to the end of the list
print(BookRatings) #output: [5, 7, 6, 8, 9, 10, 4, 3, 2]    

 

#iterating lists

top_cities = ['New York', 'London', 'Tokyo', 'Paris']
for city in top_cities:
    print(city) #output: New York London Tokyo Paris

top_cities = ['New York', 'London', 'Tokyo', 'Paris']
print(len(top_cities)) #output: 4
for cityIndex in range(len(top_cities)):
    print(f"current index is {cityIndex} and current city is {top_cities[cityIndex]}") #output: current index is 0 and current city is New York, current index is 1 and current city is London, current index is 2 and current city is Tokyo, current index is 3 and current city is Paris

spendings = [32.23, 43.23, 45.72, 23.56, 13.45, 56.78]
sum = 0.0
for spending in spendings:
    sum += spending
print(f"total spendings are: {sum}") #output: total spendings are: 214.97
# Exercise 6
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
lowSpend=0
norSpend=0
higSpend=0

for spending in spendings:
    if spending < 1000.0:
        lowSpend += 1
    elif spending> 2500.0:
        higSpend +=1
    else:
        norSpend +=1
print(f"Numbers of months with low spendings: {lowSpend}, normal spendings: {norSpend}, high spendings: {higSpend}") 
#output: Numbers of months with low spendings: 1, normal spendings: 6, high spendings: 5


#list change positions

first = input('enter first value: ')
second = input('enter second value: ')
print(f"before changing positions: first value is {first} and second value is {second}")
temp = first
first = second
second = temp
print(f"after swapping : {first}, {second}")

first = input('enter first value: ')
second = input('enter second value: ')
print(f"before changing positions: first value is {first} and second value is {second}")
first, second = second, first
print(f"after swapping : {first}, {second}")

top_cities = ['New York', 'London', 'Tokyo', 'Paris']
top_cities[0], top_cities[-1] = top_cities[-1], top_cities[0]
print(top_cities) #output: ['Paris', 'London', 'Tokyo', 'New York']

top_cities = ['New York', 'London', 'Tokyo', 'Paris']
top_cities.sort()
print(top_cities) #output: ['London', 'New York', 'Paris', 'Tokyo'] 

random_numbers = [5, 2, 9, 1, 5, 6]
random_numbers.sort()
print(random_numbers) #output: [1, 2, 5, 5, 6, 9]
random_numbers.sort(reverse=True)
print(random_numbers) #output: [9, 6, 5, 5, 2, 1]

top_cities = ['New York', 'London', 'Tokyo', 'Paris']
print(sorted(top_cities)) #output: ['London', 'New York', 'Paris', 'Tokyo'] --> this will return a new sorted list without modifying the original list
print(top_cities) #output: ['New York', 'London', 'Tokyo', 'Paris'] --> original list is not modified

# list checking presence 
for char in 'happy birthday':
    print(char) #output: h a p p y   b i r t h d a y

invited_guests = ['Alice', 'Bob', 'Charlie', 'David']
name = input('enter your name: ')
if name in invited_guests:
    print('you are invited to the party')
else:    print('you are not invited to the party')

invited_guests = ['Alice', 'Bob', 'Charlie', 'David']
name = input('enter your name: ').capitalize()
if name not in invited_guests:
    print(f'{name} is not invited to the party')
else:    print(f'{name} is invited to the party')
# copying lists

name_original = 'john'
name_New = name_original #output: name_New is john
name_original = 'michael' #output: name_New is michael
print(f"name_original is {name_original} and name_New is {name_New}") 

listOriginal = ['a', 'b', 'c']
listNew = listOriginal #output: listNew is ['a', 'b', 'c']
listOriginal[0]= 'x' #output: listNew is ['x', 'b', 'c']
print(f"listOriginal is {listOriginal} and listNew is {listNew}") 

listOriginal = ['a', 'b', 'c']
listNew = listOriginal[:] #output: listNew is ['a', 'b', 'c']
listOriginal[0]= 'x' #output: listNew is ['a', 'b', 'c']
print(f"listOriginal is {listOriginal} and listNew is {listNew}") 

listOriginal = ['a', 'b', 'c']
listNew = listOriginal[:2] #output: listNew is ['a', 'b']
listOriginal[0]= 'x' #output: listNew is ['a', 'b']
print(f"listOriginal is {listOriginal} and listNew is {listNew}") 

# list comprehensions

numbers = [1, 2, 3, 4, 5]
numbers=[]
for i in range (1,101):
    numbers.append(i)
print(numbers) #output: [1, 2, 3, 4, 5, ..., 100]

numbers = [i for i in range(1,101)]
print(numbers) #output: [1, 2, 3, 4, 5, ..., 100]

numbers = [i for i in range(1,101) if i % 3 !=0]
print(numbers) 


# Nested list 

cells = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3']]
cells[0] #output: ['a1', 'a2', 'a3']
cells[0][1] #output: 'a2'

for x in cells:
    print (f"elements: {x}") #output: elements: ['a1', 'a2', 'a3'] and elements: ['b1', 'b2', 'b3']

for x in cells:
    for y in x:
        print(f"elements: {y}") #output: elements: a1, elements: a2, elements: a3, elements: b1, elements: b2, elements: b3

table = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3']]
for row in table:
    for cell in row:
        print(cell, end=' ') #output: a1 a2 a3 b1 b2 b3

table =[[i for i in range(1,6)] for j in range(4)]
print(table) #output: [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

# adding  and multiplying lists

listUS = ['new york', 'los angeles', 'chicago']
listUK = ['london', 'manchester', 'birmingham']
listall = listUS + listUK
print(listall) #output: ['new york', 'los angeles', 'chicago', 'london', 'manchester', 'birmingham']

listNum = [0, 1] * 10
print(listNum)
# further string features

fav = 'green day'
print(fav[6]) #output: d
print(fav[:6]) #output: y
#fav[6] = 'M' #output: TypeError: 'str' object does not support item assignment --> this is because strings are immutable, you cannot change a character in a string

userNum = input('enter a number: ')
if userNum.isnumeric():
    print('you entered a valid number')
else:
    print('you did not enter a valid number')
    
'''
# Introduction to tuples

# Lists are mutable & tuples are immutable

emptyTuple = ()
oneElementTuple = (1,)
twoElementTuple = (1, 2)
threeElementTuple = 1, 2, 3
print(oneElementTuple,"\n", twoElementTuple, "\n", threeElementTuple) #output: (1,) (1, 2) (1, 2, 3)

userData = ('John', 30, 'USA')
userData[0] #output: 'John'
userData[1] #output: 30
#userData.append('UK') output AttributeError: 'tuple' object has no attribute 'append' 
