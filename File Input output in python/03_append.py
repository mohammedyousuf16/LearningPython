# append to file jonh.txt and add few more lines

f= open('john.txt', 'a')
string= ''' 
He is also looking for the job related to AI engineer

he has mastered the basic and intermediate level of python'''
f.write(string)
f.close()