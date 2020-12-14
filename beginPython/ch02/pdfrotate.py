import PyPDF2

minutesFile = open(r'E:\temp4\page8.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

page = pdfReader.getPage(0)
page.rotateClockwise(270)  # 页面旋转90度
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open(r'E:\temp4\page8r.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()


from PyPDF2 import PdfFileWriter, PdfFileReader

writer = PdfFileWriter()

reader1 = PdfFileReader(r'E:\temp4\page1r.pdf')
pages1 = reader1.getPage(0)
writer.addPage(pages1)
reader2 = PdfFileReader(r'E:\temp4\page2r.pdf')
pages2 = reader2.getPage(0)
writer.addPage(pages2)
reader3 = PdfFileReader(r'E:\temp4\page3r.pdf')
pages3 = reader3.getPage(0)
writer.addPage(pages3)
reader5 = PdfFileReader(r'E:\temp4\page5r.pdf')
pages5 = reader5.getPage(0)
writer.addPage(pages5)
reader6 = PdfFileReader(r'E:\temp4\page6r.pdf')
pages6 = reader6.getPage(0)
writer.addPage(pages6)
reader7 = PdfFileReader(r'E:\temp4\page7r.pdf')
pages7 = reader7.getPage(0)
writer.addPage(pages7)
reader8 = PdfFileReader(r'E:\temp4\page8r.pdf')
pages8 = reader8.getPage(0)
writer.addPage(pages8)
reader9 = PdfFileReader(r'E:\temp4\page9r.pdf')
pages9 = reader9.getPage(0)
writer.addPage(pages9)

with open(r'E:\temp4\outall.pdf','wb') as fh:
    writer.write(fh)