from unicodedata import name
import fitz
import re
import os



class Redactor:
    
	# static methods work independent of class object
	@staticmethod
	def get_sensitive_data(lines,data_list):
		special_acc_no = []
		special_acc_no_flag = []
		""" Function to get all the lines """
		
		# email regex
		EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
		email = re.compile(EMAIL_REG,re.IGNORECASE)

		IFSC_CODE = r"([A-Z]{4}0[A-Z0-9]{6})"
		ifsc=re.compile(IFSC_CODE,re.IGNORECASE)

		ACC_REG=r"(0*[0-9]{9,18})"
		acc_no=re.compile(ACC_REG,re.IGNORECASE)

		CARD_REG = r"([0-9]{4}[\s\-][0-9]{4}[\s\-][0-9]{4}[\s\-][0-9]{4})"
		card=re.compile(CARD_REG,re.IGNORECASE)
    	
		PAN_REG = r"([A-Z]{4}(A|B|C|F|G|H|L|J|P|T){1}[0-9]{4}[A-Z]{1})"
		pan=re.compile(PAN_REG,re.IGNORECASE)

		PHONE_REG = r"([0-9]{5}\s[0-9]{5})"
		phone_no = re.compile(PHONE_REG, re.IGNORECASE)

		PHONE_REG2 = r"(\+91\s?[0-9]{5}[0-9]{5})"
		phone_no_plus = re.compile(PHONE_REG2)

		ACC_TAG = r"Account\s?(Number)?(no)?\.?\s?\:?\s?([0-9]{9,18})"
		acc_tag=re.compile(ACC_TAG,re.IGNORECASE)

		ACC_DASH = r"Account\s?(Number)?(no)?\.?\s?\:?\s?(\w+\-\s?\w+\-\w+)"
		acc_dash=re.compile(ACC_DASH,re.IGNORECASE)


		for line in lines:
			redacted_acc_like_nos = []
			# matching the regex to each line
			if "ifsc_code" in data_list:
    				
				if ifsc.search(line):
					search = ifsc.search(line)
					
					# yields creates a generator
					# generator is used to return
					# values in between function iterations
					yield search.group(1)

			if "acc_no" in data_list:
    				
				if acc_no.search(line):
					search = acc_no.search(line)
					
					# yields creates a generator
					# generator is used to return
					# values in between function iterations
					redacted_acc_like_nos.append(search.group)
					yield search.group(1)

			if "email" in data_list:
				if email.search(line):
					search = email.search(line)
					yield search.group(1)

			if "card_no" in data_list:
				if card.search(line):
					search = card.search(line)
					yield search.group(1)
			
			if "pan_no" in data_list:
				if pan.search(line):
					search = pan.search(line)
					yield search.group(1)

			if "acc_tag" in data_list:
				if acc_tag.search(line):
					search = acc_tag.search(line)
					acc_no_temp = search.group(3)
					if acc_no_temp and acc_no_temp not in redacted_acc_like_nos:
						redacted_acc_like_nos.append(acc_no_temp)
						yield acc_no_temp
			
			if "acc_dash" in data_list:
				s = acc_dash.search(line)
				if s:
					special_acc_no.append(s.group(3))
					for x in special_acc_no:
						comp_dashed_acc_no = re.compile(x)
						search = comp_dashed_acc_no.search(line)

						if search.group():
							yield search.group()
					
					if acc_dash.search(line):
						search = acc_dash.search(line)
						yield search.group(1)

			if "phone_no" in data_list:
				if phone_no.search(line):
					search = phone_no.search(line)
					temp_ph_no = search.group(1)
					if temp_ph_no not in redacted_acc_like_nos:
						redacted_acc_like_nos.append(search.group(1))
						yield search.group(1)
				elif phone_no_plus.search(line):
					search = phone_no_plus.search(line)
					temp_ph_no = search.group(1)
					if temp_ph_no not in redacted_acc_like_nos:
						redacted_acc_like_nos.append(search.group(1))
						yield search.group(1)

			
			# if "name" in data_list:
			# 	if name_tag.search(line):
			# 		search = name_tag.search(line)
			# 		yield search.group(1)

	# constructor
	def __init__(self, path,data_list):
		self.path = path

	def redaction(self,data_list,black_bar):
	
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
				if black_bar:
					[page.add_redact_annot(area, fill = (0, 0, 0)) for area in areas]
				else:
					[page.add_redact_annot(area,text = "X"*len(data), fill = (1, 1, 1)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		if black_bar:
			doc.save('output/'+os.path.basename(self.path)[:-4]+'-redacted-black.pdf')
		else:
			doc.save('output/'+os.path.basename(self.path)[:-4]+'-redacted-masked.pdf')
		# saving it to a new pdf
		
		print("Successfully redacted")