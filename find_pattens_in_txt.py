from pii_regex import find_pan_in_text, find_aadhar_in_text, find_ifsc_in_text, find_acc_no_in_text, \
    find_entities_with_prefixes, find_phone_number_in_text

filepath = "sample.txt"
text_file = open(filepath ,"r")

text_content = text_file.read()

print(find_entities_with_prefixes(text_content))
print(find_pan_in_text(text_content))
print(find_aadhar_in_text(text_content))
print(find_phone_number_in_text(text_content))
print(find_ifsc_in_text(text_content))




