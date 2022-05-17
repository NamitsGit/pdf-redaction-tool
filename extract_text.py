import os
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()

def extract_text_from_pdf(filename):
    inp_file = filename

    if not os.path.exists(inp_file):
        raise Exception("The given input path \'"+inp_file+"\' of the pdf file does not exist.\nRe-enter the file path and try again.")

    if not os.path.isfile(inp_file):
        raise Exception("The given input path \'"+inp_file+"\' does not correspond to a filename.\nRe-enter the file path to include the proper filename.")

    with open(inp_file, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    out_file = 'extracted_' + os.path.basename(inp_file)[:-4] +'.txt'
    with open(os.path.basename(out_file), mode='w') as f:
        print(output_string.getvalue(), file=f)

    print("The file written is :   "+out_file)

# SAMPLE
# extract_text_from_pdf('test/statement_sample1-Copy1.pdf')
