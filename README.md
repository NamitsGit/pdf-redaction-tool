# doc-parser
Hello all,
doc parser is a document parser whose objective will be to parse PDF files, look for **PIIs and other confidential information** in the PDF files and **redact** that information in the **original PDF file** accordingly. 
It should basically work as a **confidential information redaction tool**.

**For example**: If an Aadhar Number(Indian Unique ID number) is found in a document, it should redact that number, something like this:
Aadhar Number: 0123 4567 8910 -->  XXXX XXXX XXXX


## File Information
| Filename | Description |
| :--- | :--- |
| pii_regex.py | Used to find patterns in text like PAN, Aadhar, IFSC code, Phone Number, People names, etc. |
| test_regex.py | Used to test the regex patterns on sample plain text(meant to be used after text extraction from pdf files) |

