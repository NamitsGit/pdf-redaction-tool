# PROJECT DOCUMENTATION
------------

## Problem Statement
<br>For Redaction, build an alternative tool that can replace the sensitive content of pdf with redacted data as per user choice for mechanism of redaction. The current redactor speed has scope for improvement.

### Exploration
**Week 1:** Went through related **scientific/technical papers** and articles regarding different **methods of redaction** used for born-digital documents, and learnt about the use of **regular expression** for finding text of a certain pattern. </br>

<br>**Week 2:** Tried implementation of josh pdf-redactor. Discussion about finding **PIIs from different buckets**. Tried finding regexes of common PIIs in plain text like PAN, Aadhar, IFSC Code, Bank account number, etc.
Also implemented basic methods of conversion of pdf to plain text(Text Extraction) and tried to understand **Named Entity Recognition** and its use in our current project.</br>

<br>**Week 3:** Searched for different modules and methods available for **modification of pdf**, tried extraction of pdf files with python modules. Basic implementation of **regex patterns** that would be applicable.</br>

<br>**Week 4:** Pattern identification of first 3 buckets of different types implemented. Identification of **orphan text** with salutations can be identified. Implementation of NER tried by using spacy. PDF layout aware modification tried.
**PyMuPDF utilities** explored, also explored other functionalities of pdfrw for pdf modification.
**Layout analyzer** utility of PyMuPDF implemented to extract the layout of pdf files. Other demos and examples explored.</br>

<br>**Week 5:**
Explored about metadata of PDF files.
Tried code related to annotations.
Tested different pdf modification techniques based on annotations and implemented different regrex patterns on the sample files.
<br>

<br>**Week 6:**
Tried code related to characters stream extraction and editing.
Learnt different methods of modifying the characters stream.
<br>

<br>**Week 7:**
Tried and tested code on some other sample bank statements, and made minor corrections in regular expressions.
Tried to redact orphan data like addresses and names.
<br>

<br>**Week 8:**
Tried methods to correct problems faced during redaction of orphan data.Tried PyMuPDF codes and went through pdfrw to perform modifications in pdf files PyMupdf.
<br>

<br>**Week 9:**
PyMuPDF utilities explored, also explored other functionalities of pdfrw for pdf modification. Layout analyzer utility of PyMuPDF implemented to extract the layout of pdf files. Other demos and examples explored.
<br>

<br>**Week 10:**
Tried test cases with pdfrw. Tested the code with some samples.Mid term presentation slides preparation.
<br>

<br>**Week 11:**
Mid Term presentation. Tried pdfrw approach with the new sample files. Found a new method using pymupdf. Tried to redact using MuPDF. Tried the MuPDF approach with all test files. Measured and compared times for both the methods.
<br>

<br>**Week 12:**
Optimized the PyMuPDF approach. Tried to reduce overlapping issues with MuPDF by reducing redundant regexes. Understood about flaskx, flaskrestplus and other related libraries.
<br>

<br>**Week 13:**
Tried a few more test cases. Applied the project structure. Learned about swagger.ui and made API calls to run the redaction as a web api service. Prepared for final presentation.
<br>

### Design
Involves use of library PyMuPDF for redaction of pdf documents.
Read the PDF file
Iterate line by line through the pdf and look for each occurrence of PIIs. PIIs have a pattern, so we will be using Regex to identify a PII
Once we encounter a PII, we yield it from within the loop.
Now, we need to simply search for the occurrence of the fetched PIIs in the pdf. PyMuPDF makes it very easy to find any text in a PDF. It returns four coordinates of a rectangle inside which the text will be present.
Once we have all the text boxes, we can simply iterate over those boxes and Redact each box from the PDF


### Code
Within the app folder.


### Testing
Within app/tests

### POC, Iteration, Project Validation
TBD


