import PyPDF2
a = PyPDF2.PdfFileReader('resume.pdf')
print(a.documentInfo)
print(a.getNumPages())
print(a.getPage(0).extractText())

# def extract_text_from_pdf('resume.pdf'):
#     try:
#         with open(pdf_path, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#             text = ""
#             for page_num in range(pdf_reader.numPages):
#                 page = pdf_reader.getPage(page_num)
#                 text += page.extractText()
#             return text
#     except Exception as e:
#         return str(e)
    
# print(str)