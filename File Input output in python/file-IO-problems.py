'''
# Question 1
# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
# Open notes.txt , read its content, and print it to the console.

with open('notes.txt', 'w') as f:
    string="Learning Python is fun!"
    f.write(string)

with open('notes.txt', 'r') as f:
    data= f.read()
    print(data)

# Question 2
# Write a program that writes three lines of text to a file tasks.txt .
# Open tasks.txt in append mode and add a new line "Task Completed!" .
# Read the file and print all lines as a list using readlines() .

with open('task.txt', 'w') as f:
    data= 'This is the first line \nthis is the middle line \nthis is the final and last line '
    f.write(data)

with open('task.txt', 'a') as f:
    f.write(f'\n Task Completed!')

with open('task.txt', 'r') as f:
    data=f.read()
    print(data)
'''


# Question 3

# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder

import os
print(os.getcwd())
print(os.listdir())
os.mkdir('myfolder')