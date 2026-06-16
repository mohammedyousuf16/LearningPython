import os
a = os.listdir('dir')
print(a) # output: ['test2.txt', 'sub', 'test.txt']

# to get the current directory
print(os.getcwd()) 
print(os.path.exists('dir')) #output: True
print(os.path.exists('master')) #output: False

os.remove('dir/sample.txt') # removes the files
os.rmdir('dir/sub') # removes the directory
