

from io import StringIO
import string
import fitz
import re
import json
from flask import Flask,request

app = Flask(__name__)
output=""

a={ "outpath" : r"C:\Users\arvin\Desktop\api\output" }
p=a["outpath"]

@app.route("/result",methods=["Post","Get"])
def result():
		output = request.get_json()
		path=output["filepath"]
		dataf=output["data_fields"]
		data_dict = json.dumps(output["data_fields"])
		redactor = Redactor(path,data_dict)
		redactor.redaction(data_dict)
		
		
		cal = {}
		cal['redacted_filepath'] = p
		return (cal)

class Redactor:

	# static methods work independent of class object
	@staticmethod
	def get_sensitive_data(lines,data_dict):
	
		""" Function to get all the lines """
		
		# email regex
		EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
		IFSC_CODE = r"([A-Z]{4}0[A-Z0-9]{6})"
		ACC_REG=r"(0*[0-9]{9,18})"
		for line in lines:
		
			# matching the regex to each line
			if "ifsc_code" in data_dict:
    				
				if re.search(IFSC_CODE, line, re.IGNORECASE):
					search = re.search(IFSC_CODE, line, re.IGNORECASE)
					
					# yields creates a generator
					# generator is used to return
					# values in between function iterations
					yield search.group(1)

			if "acc_no" in data_dict:
    				
				if re.search(ACC_REG, line, re.IGNORECASE):
					search = re.search(ACC_REG, line, re.IGNORECASE)
					
					# yields creates a generator
					# generator is used to return
					# values in between function iterations
					yield search.group(1)

	# constructor
	def __init__(self, path,data_dict):
		self.path = path

	def redaction(self,data_dict):
	
		""" main redactor code """
		
		# opening the pdf
		doc = fitz.open(self.path)
		
		# iterating through pages
		for page in doc:
		
			# _wrapContents is needed for fixing
			# alignment issues with rect boxes in some
			# cases where there is alignment issue
			page.wrap_contents()
			
			# getting the rect boxes which consists the matching email regex
			sensitive = self.get_sensitive_data(page.get_text("text")
												.split('\n'),data_dict)
			for data in sensitive:
				areas = page.search_for(data)
				
				# drawing outline over sensitive datas
				[page.add_redact_annot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		# saving it to a new pdf
		doc.save('output/redacted1.pdf')
		print("Successfully redacted")

# driver code for testing
if __name__ == "__main__":
    app.run(debug=True,port=2000)
     # path = 'tests/CAAxis1.pdf'
   















