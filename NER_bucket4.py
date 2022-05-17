import en_core_web_sm
nlp = en_core_web_sm.load()

#NAME OF THE TEXT FILE
text_file = open("stmt_sample.PDF.txt")
data = text_file.read()

text_file.close()
doc = nlp(data)

for X in doc.ents:
    if X.label_ == "PERSON":
        print(X.text,X.label_)

