import os
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
inp_file = "statement_sample1-Copy1.PDF"

with open(inp_file, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)


print(output_string.getvalue())

out_file = 'extracted_' + os.path.basename(inp_file)[:-4] +'.txt'
with open(os.path.basename(out_file), mode='w') as f:
    print(output_string.getvalue(), file=f)

print("The file written is :   "+out_file)