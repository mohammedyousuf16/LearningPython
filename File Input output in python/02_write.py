# write a file jonh.txt about him

f= open('john.txt', 'w')
string= ''' john is a full stack developer with MERN as his skill set

now he want to learn python for scripting and the AI related work.'''
f.write(string)
f.close()