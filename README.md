# doc-parser
Hello all,
doc parser is a document parser whose objective will be to parse PDF files, look for **PIIs and other confidential information** in the PDF files and **redact** that information in the **original PDF file** accordingly. 
It should basically work as a **confidential information redaction tool**.

**For example**: If a debit card number is found in a document, it should redact that number, something like this:
Card Number: 0123-4567-8910-1234 -->  XXXX-XXXX-XXXX-XXXX


## File Information
| Filename | Description |
| :--- | :--- |
| pii_regex.py | Used to find patterns in text like PAN, Aadhar, IFSC code, Phone Number, People names, etc. |
| extract_text.py | Used to extract text from a pdf file and store the text of pdf file into a .txt file with the same filename. |
