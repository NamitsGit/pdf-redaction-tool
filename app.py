import json
from flask import Flask, request
from flask_restx import Api, Resource, fields
import re
import fitz
import os

app = Flask(__name__)
api = Api(app )#,doc=False

api.title =  "PDF REDACTOR"
ns = api.namespace('', description='This is the Pdf redactor')
a_input = api.model('Inputs', {'filepath' : fields.String('Your file path'),"datafields":fields.String('PIIs')}) #, 'id' : fields.Integer('ID')
 
directory = "output"
parent_dir = os.getcwd()
p = os.path.join(parent_dir, directory) 
try:
    os.makedirs(p, exist_ok = True)
    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created" % directory)

@ns.route('/')
class Resdac(Resource):



    @api.expect(a_input)
    def post(self):
        output = request.get_json()
        path=output["filepath"]
        data_list=output["data_fields"]
 #       data_list = json.dumps(output["datafields"])
        redactor = Redactor(path,data_list)
        redactor.redaction(data_list)
        return {'result' : p}, 201 

class Redactor:
    
	# static methods work independent of class object
	@staticmethod
	def get_sensitive_data(lines,data_list):
	
		""" Function to get all the lines """
		
		# email regex
		EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"

		IFSC_CODE = r"([A-Z]{4}0[A-Z0-9]{6})"
		ifsc=re.compile(IFSC_CODE,re.IGNORECASE)

		ACC_REG=r"(0*[0-9]{9,18})"
		accno=re.compile(ACC_REG,re.IGNORECASE)

		for line in lines:
		
			# matching the regex to each line
			if "ifsc_code" in data_list:
    				
				if ifsc.search(line):
					search = ifsc.search(line)
					
					# yields creates a generator
					# generator is used to return
					# values in between function iterations
					yield search.group(1)

			if "acc_no" in data_list:
    				
				if accno.search(line):
					search = accno.search(line)
					
					# yields creates a generator
					# generator is used to return
					# values in between function iterations
					yield search.group(1)

	# constructor
	def __init__(self, path,data_list):
		self.path = path

	def redaction(self,data_list):
	
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
												.split('\n'),data_list)
			for data in sensitive:
				areas = page.search_for(data)
				
				# drawing outline over sensitive datas
				[page.add_redact_annot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		# saving it to a new pdf
		doc.save('output/'+os.path.basename(self.path)[:-4]+'-redacted.pdf')
		print("Successfully redacted")

if __name__ == '__main__':
    app.run(debug=True)