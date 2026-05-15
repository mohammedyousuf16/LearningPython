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
'''
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