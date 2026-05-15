# introduction to functions
'''
def greet():
    print('Hello World from a function!')
greet()

# functions with parameters

inputNumber = [5.0, 19.8, 3.14, 2.71, 23.9]
def getAverage(Number):
    sum = 0
    for num in Number:
        sum += num
    average = sum / len(Number)
    print(average)

getAverage(inputNumber)

def printLetterCount(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    print(count)

printLetterCount('hello world, welcome to my world of python learning that i have started', 'e')
# default parameters values

print('hello', 'how are you?', end='\n', sep='-')

def printLetterCount(text='this is a default string', letter='a'):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    print(count)

printLetterCount('how many letters a are in this sentence?')
printLetterCount()
#name scope
def showTruth():
    #global mistry #global variable now this will make the local variable to gloabl variable
    mistry = 'The cake is a lie' #local variable shawows the global variable
    print(mistry)
mistry = 'The cake is not a lie' #global variable
showTruth()
#The None value

printReturn = print('hello world')
print(printReturn)

x= None

if x:
    print('true')
elif x is False:
    print('False')
else:
    print('x is not true nor false') #output x is not true nor false

if x is None:
    print('yes')
if x == None:
    print('it does')

def greet():
    print('i will return None value')

x= greet()
print(x)
'''
'''
# Return Keyword

def getAverage(inputNum):
    sum = 0.0
    for num in inputNum:
        sum += num
    average = sum / len(inputNum)
    return average
print('The average is :', getAverage ([5.0, 2.5, 2.6, 9.2]))

average = getAverage([5.0, 2.5, 2.6, 9.2])
if average > 4.0:
    print('the average is too high:' , average)

def gatave(inputnum):
    sum = 0.0
    for num in inputnum:
        sum += num
    average = sum / len(inputnum)
    return average
    print('this line will not be printed as it come after the return')

ave =gatave([2, 3, 5])
print(ave)
# exercise 9
def unique(lists):
    uniqueList=[]
    for item in lists:
        if item not in uniqueList:
            uniqueList.append(item)
    print(uniqueList)
            
unique([1, 1, 4, 5, 1])
unique(['Mark', 'Mark', 'John', 'Anne'])
unique([1,2,3,3,3,3,4,5])


# Recursion 

# factorial
# 3! = 1 * 2 * 3 = 6
# 5! = 1 * 2 * 3 * 4 * 5 = 120


# Iterative function
def getFactorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial
print(getFactorial(5)) #output: 120

# Recursive function

def getFactorialRecursive(num):
    if num <=1:
        return 1
    return num * getFactorialRecursive(num -1)
print(getFactorialRecursive(5))

# Generators

def get_num():
    for i in range(1,4):
        yield i 
generate= get_num()
print(next(generate))
print(next(generate))
print(next(generate))

for x in get_num():
    print(x)

number = list(get_num())
print(number)

''' 
# exceptions - intro

try:
    value = int(input('enter an integer'))
    print(f"The inverse of {value} is {1/value}")
except:
    print('you did not enter an integer')

try:
    value = int(input('enter an integer'))
    print(f"The inverse of {value} is {1/value}")
except ValueError:
    print('you did not enter an integer')
except ZeroDivisionError:
    print('you provided 0 and division by 0 is not possible, sorry')

try:
    value = int(input('enter an integer'))
    print(f"The inverse of {value} is {1/value}")
except ValueError:
    print('you did not enter an integer')
except ZeroDivisionError:
    print('you provided 0 and division by 0 is not possible, sorry')
except:
    print('something strange happend here, sorry')