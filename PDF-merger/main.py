from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs=[]
n = int(input('enter the number of pdf to merge\n '))

for i in range(0,n):
    name= input(f'Enter the name of PDF {i + 1}: ')
    print(i)
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)

merger.write('merged-PDF.pdf')
merger.close()