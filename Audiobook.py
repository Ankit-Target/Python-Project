import pyttsx3
import PyPDF2
book = open("oop.pdf" , "rb" )
pdfReader = PyPDF2.PdfReader(book) 
pages = len(pdfReader.pages)
print(pages)
engine = pyttsx3.init()
page = pdfReader.pages[0]
text = page.extract_text()
print(page, type(page))
engine.say(text)
engine.runAndWait()