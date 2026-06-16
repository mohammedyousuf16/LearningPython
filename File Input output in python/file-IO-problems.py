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


# Question 3

# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder

import os
print(os.getcwd())
print(os.listdir())
os.mkdir('myfolder')

# Question 4

# Use the shutil module to:
# Copy a file from one folder to another
# Move a file to a new folder
# Delete a file (careful: irreversible!)

import shutil
shutil.copy('jonny.txt', 'dir/')
shutil.move('notes.txt','myfolder')
shutil.rmtree('dir/')


# Question 5
# Write a small script count_lines.py that takes a filename as input and prints
# how many lines are in the file.
# Example usage:
# python count_lines.py tasks.txt
# Output: Number of lines: 4

import sys

def countLines(filename):
    with open(filename) as f:
        return  len(f.readlines())


if (__name__)== "__main__":
    filename= sys.argv[1]
    num_lines= countLines(filename)
    print(f'the number of lines are: {num_lines} in {filename}')
'''


# Question 6

# Write a command-line utility search_word.py that takes two arguments:
# A filename
# A word to search and prints how many times the word appears in the file.

import sys

def countWords(word, string):
    pass

if __name__ == "__main__":
    filename = sys.argv[1]
    word = sys.argv[2]
    with open(filename)as f:
        string= f.read()
        n= string.count(word)
        print(f'there are {n} time the word:\'{word}\' in the {filename}')