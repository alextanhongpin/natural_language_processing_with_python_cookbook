from PyPDF2 import PdfFileReader

def get_text(filename, password=''):
    pdf_file = open(filename, 'rb')
    read_pdf = PdfFileReader(pdf_file)
    if password != '':
        read_pdf.decrypt(password)
    
    text = []
    for i in range(0, read_pdf.getNumPages()):
        text.append(read_pdf.getPage(i).extractText())
    
    return '\n'.join(text)