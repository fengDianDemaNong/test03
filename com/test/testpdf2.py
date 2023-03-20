from PyPDF4 import PdfFileReader

with open('test.pdf','rb') as f:
    pdf=PdfFileReader(f)
    information=pdf.getDocumentInfo()
    number_of_pages=pdf.getNumPages()

txt=f"""Author: {information.author}
Creator: {information.creator}
Producer: {information.producer}
Subject: {information.subject}
Title: {information.title}
Number of pages: {number_of_pages}"""
print(txt)


pdffile = open('test.pdf','rb')
pdfreader = PdfFileReader(pdffile)
print(pdfreader.numPages)

# page = pdfreader.getPage(0)
# print(page.extractText().strip())


import PyPDF4
FILE_PATH = 'test.pdf'

with open(FILE_PATH, mode='rb') as f:
     reader = PyPDF4.PdfFileReader(f)
     page = reader.getPage(0)
     print(page.extractText().strip())