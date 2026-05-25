'''
There are two types of modules in python
- Built in modules
- External modules
'''
import math
import os # if you import and dont use it it will be in gray until you use it
import mymodule #you can import your own module from other py file
# you can use the pip comand to install modules and import them here
import requests

r = requests.get("https:www.google.com")
print(math.sqrt(16))
mymodule.hello()