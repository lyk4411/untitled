## pip install PyPDF2
##
# 1.打开一个或多个已有的PDF（源PDF），得到PdfFileReader对象。
# 2.创建一个新的PdfFileWriter对象。
# 3.将页面从PdfFileReader对象拷贝到PdfFileWriter对象中。
# 4.最后，利用PdfFilewriter对象写入输出的PDF

## 拷贝页面
import PyPDF2

pdf1File = open('E:\\aaa.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pageObj.rotateClockwise(180)
    pdfWriter.addPage(pageObj)
# 写入合并文件
pdfOutputFile = open('E:\\bbb.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()

## 旋转页面
import PyPDF2

minutesFile = open('E:\\aaa.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

page = pdfReader.getPage(0)
page.rotateClockwise(180)  # 页面旋转90度
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('E:\\ccc.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
