import pyttsx3
import PyPDF2
import re

# init speech engine
engine = pyttsx3.init()

# set the locale language to french 
# TODO : Propose to user languages available
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# Get the local document and open it
# TODO : create an argument to get the path of the (file to open || actual file ?)
pdfFileObj = open('Enm-2021-NdS-GE1-Sujet-Vdef.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_page = pdfReader.numPages

document_content = []

# get doc content (starting in page 3)
# TODO : Get a start reading parameter (with default value)
for i in range(2, num_page):
    p = {}
    pageObj = pdfReader.getPage(i)
    text = pageObj.extractText()
    normalized_text = text.replace('™', "’")
    removed_newlines = normalized_text.replace('\n', "") #re.sub(r"(?<=[a-z])\r?\n"," ", normalized_text) #re.sub(r"(?<=[a-z])\r?\n"," ", textblock)
    p['index'] = i
    p['content'] = removed_newlines
    document_content.append(p)

#Queue each page to read to the speech engine
for v in document_content:
    engine.say(v.get('content'))
    engine.runAndWait()