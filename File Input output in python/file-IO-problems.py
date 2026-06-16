'''
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