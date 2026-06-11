'''
# Question 1
# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!" .

def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@logger
def say_hello():
    print('Hello!')

say_hello()

'''

# Question 2

# Write a decorator timer that calculates how long a function takes to execute.
# Test it with a function that sums numbers from 1 to 1,000,000.

from time import time

def timer(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2=time()
        time_taken=f' Time taken to calculate {t2-t1}'
        return time_taken
    return wrapper

@timer
def sum(n):
    total= 0
    for i in range(1, n+1):
        total += i
    print(f'sum on {n} is {total}')
print(sum(1000000))

