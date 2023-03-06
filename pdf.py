import PyPDF2

def readPDF():
    reader = PyPDF2.PdfReader('file.pdf')
    
    #print(len(reader.pages))
    
    page = reader.pages[0]
    
    text = page.extract_text()
    
    return text