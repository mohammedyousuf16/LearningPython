'''
There are two types of modules in python
- Built in modules
- External modules

import math
import os # if you import and dont use it it will be in gray until you use it
import mymodule #you can import your own module from other py file
# you can use the pip comand to install modules and import them here
import requests

r = requests.get("https:www.google.com")
print(math.sqrt(16))
mymodule.hello()


# Sets and sets methods in python
# sets are unordered, unique collections
s = {1,3,6,9,4}

print(s, type(s))
#print(s[3]) # sets are unortdered so this will show an error
s.add(32)
s.add(324) # cant add the number which is already in the set
print(s)
s.remove(1)
s.discard(23445) # discard means only remove if the number is in the set
s.pop() # removes random elements form the set
print(s)

'''

# Set operations

a = {23,4,6,1}
b = {26, 23, 45, 5, 1}
c= a.union(b) # c has the elements from both the sets no duplicats are allowed
print(c) 
d= a.intersection(b) # d has the elements that are same in both the sets
print(d) 
e= a.difference(b) # elements in a which are not in b
f= b.difference(a) # elements in b which are not in a
print(e)
print(f)