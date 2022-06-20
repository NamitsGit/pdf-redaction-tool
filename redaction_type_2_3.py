
from io import StringIO
import string
import fitz
import re
import json
from flask import Flask ,request

app = Flask(__name__)
output =""
a={"nm" : r"/home/namit/Desktop/perfios/proj/new" }
p= a["nm"]
input1= ""
input2= ""
input3= ""


# output = request.get_json()
@app.route("/result",methods=["Post"," Get"])
def result():
    input1= request.form['path']
    input2= request.form['ifsc']
    input3= request.form['accno']
    #	path=output["name"]
    redactor = Redactor(input1,input2,input3)
    redactor.redaction(input2,input3)
    #	name = output["name"]
    cal = {}
    cal['filepath'] = p
    return (cal)


class Redactor:

    # static methods work independent of class object
    @staticmethod
    def get_sensitive_data(lines,inp2,inp3):

        """ Function to get all the lines """

        # email regex
        EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
        IFSC_REG = r"([A-Z]{4}0[A-Z0-9]{6})"
        ACC_REG = r"(0*[0-9]{9,18})"
        CARD_REG = r"([0-9]{4}\s?\-?[0-9]{4}\s?\-?[0-9]{4}\s?\-?[0-9]{4})"
        PHONE_REG = r"(\+?[0-9]{0,2}\s*[0-9]{5}\s?[0-9]{5})"
        PAN_REG = r"([A-Z]{5}[0-9]{4}[A-Z]{1})"
        NAME_MR_MS = r"([M|m][r|R|s|S][.\s]*\w+\s\w+\s?\w+)"
        NAME_TAGGED = r"Name\s?\:?\s?\w+\s?\w+"
        # ADDR_REG = r"(address\s?\:?\.*\w+\s?\,?\w+\s?\,?)"
        ADDR_REG2 = r"(([N|n][O|o])?\.?\s?\w+\s?\,?\w+\/\w+\s?[^(0-9{4})])"
        ADDR_PIN_REG = r"(\w+\,?\s?\w+\s?\-?\s?[0-9]{6})"
        # NAME_TITLE = r"(name:)"
        # NAME_MRS = r"(M[R|r][S|s][.\s]*\w+\s\w+\s?\w+)"
        # NAME_DR = r"([D|d][r|R][.\s]*\w+\s\w+\s?\w+)"
        for line in lines:

            # matching the regex to each line
            if inp2=="yes":
                if re.search(IFSC_REG, line, re.IGNORECASE):
                    search = re.search(IFSC_REG, line, re.IGNORECASE)
                    yield search.group(1)
                # yields creates a generator
                # # generator is used to return
                # values in between function iterations

            if inp3=="yes":
                if re.search(ACC_REG, line, re.IGNORECASE):
                    search = re.search(ACC_REG, line, re.IGNORECASE)
                    yield search.group(1)
                # yields creates a generator
                # # generator is used to return
                # # values in between function iterations

    # constructor
    def __init__(self, path,inp2,inp3):
        self.path = path

    def redaction(self,inp2,inp3):

        """ main redactor code """

        # opening the pdf
        doc = fitz.open(self.path)

        # iterating through pages
        for page in doc:

            # _wrapContents is needed for fixing
            # alignment issues with rect boxes in some
            # cases where there is alignment issue
            page.wrapContents()

            # getting the rect boxes which consists the matching email regex
            sensitive = self.get_sensitive_data(page.getText("text")
                                                .split('\n'),inp2,inp3)
            for data in sensitive:
                areas = page.searchFor(data)

                # drawing outline over sensitive datas
                [page.addRedactAnnot(area, fill = (0, 0, 0)) for area in areas]

            # applying the redaction
            page.apply_redactions()

        # saving it to a new pdf
        doc.save('output/redacted.pdf')
        print("Successfully redacted")


# driver code for testing
if __name__ == "__main__":
    app.run(debug=True, port=2000)
    # path = 'tests/CAAxis1.pdf'















