'''
Using QRcode library to create QR-code and convert url to QR-code
# pip install qrcode
'''
import qrcode

url = input('Enter URL to generate QR-code: ')
filename= input('input filename you want to save it as: ')
if not(filename.endswith('.png')):
    filename= filename + ".png"

img = qrcode.make(url)
img.save(filename)