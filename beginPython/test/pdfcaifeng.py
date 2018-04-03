# coding:utf8
import os

from PyPDF2 import PdfFileWriter, PdfFileReader
inputfile = r'F:\Users\lyk\PycharmProjects\untitled\beginPython\test\ab.pdf'
outputfile = r'F:\Users\lyk\PycharmProjects\untitled\beginPython\test\test\a.pdf'
reader = PdfFileReader(inputfile)
pages = [1,2,3,4,5,6,7,8,9,10,11]
getpages = list()

for i in pages:
    page = reader.getPage(i-1) #page number starts with 0
    getpages.append(page)


writer = PdfFileWriter()
for page in getpages:
    writer.addPage(page)
with open(outputfile,'wb') as fh:
    writer.write(fh)


inputfile = r'F:\Users\lyk\PycharmProjects\untitled\beginPython\test\ab.pdf'
outputfile = r'F:\Users\lyk\PycharmProjects\untitled\beginPython\test\test\b.pdf'
reader = PdfFileReader(inputfile)
pages = [1,2,12,13,14,15,16,17,18,19,20,21]
getpages = list()

for i in pages:
    page = reader.getPage(i-1) #page number starts with 0
    getpages.append(page)


writer = PdfFileWriter()
for page in getpages:
    writer.addPage(page)
with open(outputfile,'wb') as fh:
    writer.write(fh)