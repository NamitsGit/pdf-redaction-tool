# PROJECT DOCUMENTATION
------------
## PROJECT 1 : Overall Plan

<br>Week 1 - 2 ->  Exploring</br>
<br>Week 3 -> Design </br>
<br>Week 4 - 5 -> Code </br>
<br>Week 6 - 7 -> Testing </br>
<br>Week 8 -> POC, Iteration, Project Validation </br>
<br>**TOTAL 60 days [2 months]**

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
Tried methods to correct problems faced during redaction of orphan data.
<br>

### Design
TBD

### Code
TBD



### Testing
TBD

### POC, Iteration, Project Validation
TBD


