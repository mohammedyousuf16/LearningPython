with open('john.txt', 'r') as f:
    data= f.read()
    print(data)

with open('sample.txt', 'w') as f:
    string= ''' This is opened in write mode and all the data in the file will be wiped and the new data will be pasted inside'''
    f.write(string)

with open('sample.txt', 'a') as f:
    f.write('  THIS IS FROM THE APPEND WHICH WAS OPENED WITH THE "WITH" KEYWORD')
