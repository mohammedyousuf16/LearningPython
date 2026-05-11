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
