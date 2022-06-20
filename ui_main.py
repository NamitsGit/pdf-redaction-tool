

from io import StringIO
import string
import fitz
import re
import json
from flask import Flask,request

app = Flask(__name__)
output=""

a={ "nm" : r"C:\Users\arvin\Desktop\api" }
p=a["nm"]
input1=""
input2=""
input3=""
# output = request.get_json()
@app.route("/result",methods=["Post","Get"])
def result():
	input1=request.form['path']
	input2=request.form['ifsc']
	input3=request.form['accno']
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
		IFSC_CODE = r"([A-Z]{4}0[A-Z0-9]{6})"
		ACC_REG=r"(0*[0-9]{9,18})"
		for line in lines:
		
			# matching the regex to each line
			if inp2=="yes":
				if re.search(IFSC_CODE, line, re.IGNORECASE):
					search = re.search(IFSC_CODE, line, re.IGNORECASE)
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
    app.run(debug=True,port=2000)
     # path = 'tests/CAAxis1.pdf'
   















