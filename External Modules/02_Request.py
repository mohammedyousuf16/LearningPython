import requests

r= requests.get('https://api.github.com/users/mohammedyousuf16')


with open('yousuf.txt', 'w') as f:
    data= r.text
    f.write(r.text)