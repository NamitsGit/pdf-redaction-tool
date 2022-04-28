from pii_regex import find_pan_in_text, find_aadhar_in_text, find_ifsc_in_text, find_acc_no_in_text, \
    find_entities_with_prefixes, find_phone_number_in_text

print(find_pan_in_text(' asdflkjsldj AAAAA8864G'))
print(find_pan_in_text('hello this is a sample text KELIO9983W'))
print(find_pan_in_text('AAAAA'))
print(find_pan_in_text('AAAAA----'))
print(find_pan_in_text('AAAAA886LG'))

print(find_aadhar_in_text('aldsfj;lsjd l 3675 9834 6015'))
print(find_aadhar_in_text('Hello the aadhar number is 3675 9834 6015'))
print(find_aadhar_in_text('Hello the aadhar number is 3675-9834-6015'))

print(find_ifsc_in_text('Hello the ifsc code is : SBIN00A0320'))
print(find_ifsc_in_text('IFSC No: ICIC00B0215'))
print(find_ifsc_in_text('Hello there is  no IFSC here'))

print(find_acc_no_in_text('Hello account number is : 123456789'))
print(find_acc_no_in_text('Hello account number is : 1234567890'))
print(find_acc_no_in_text('Hello account number is : 123456789012'))
print(find_acc_no_in_text('Hello account number is : 12345678965464'))

print("\n\n\n")
s = "PAN: KELIO9983W   HIEJK3456P \nAadhar: 3675 9834 6015\nAadhar2: 351285479658\nAadhar3: 3675-9834-6015\nIFSC No: SBIN00A0320 ICIC00Z4824 \nAccount No: 123456789012 00000000043534 0s000078937939"
print(find_pan_in_text(s))
print(find_aadhar_in_text(s))
print(find_ifsc_in_text(s))
print(find_acc_no_in_text(s))

print("\n\n\n\n\n")
sample2 = "Monthly bank statement of Mr.Virat Kohli"
sample3 = "Yearly savings account statement of Mr.Mahendra Singh Dhoni"
sample4 = "Monthly bank statement of Mr.Ramnath Kovind"
sample5 = "Yearly savings account statement of Mr. K L Rahul"
sample6 = "Quaterly savings account statement of Mr......Robin Utthappa"
sample6 = "Quaterly savings account statement of MR     AMITABH BACHCHAN"

sample7 = "Monthly bank statement of Ms.Shraddha Kapoor"
sample8 = "Yearly savings account statement of Ms.Rashmika K Mandanna"
sample9 = "Monthly bank statement of Mrs.Vimala Kovind"
sample10 = "Yearly savings account statement of Ms. Athiya S Shetty"
sample11 = "Quaterly savings account statement of Mrs......Aditi Menon"
sample12 = "Quaterly savings account statement of MRS     Aishwarya Rai Bachchan"


sample13 = "Phone number of Mr. Virat Kohli is +91 9535684521"
sample14 = "Phone number of Mr. Virat Kohli is +91 95356 84521"
sample15 = "Phone number of Mr. Virat Kohli is 9535684521"
sample16 = "Phone number of Mr. Virat Kohli is                     95356 84521"
sample16 = "Phone number of Mr. Virat Kohli is                     +1 95356 84521"

print(find_entities_with_prefixes(sample2))
print(find_entities_with_prefixes(sample3))
print(find_entities_with_prefixes(sample4))
print(find_entities_with_prefixes(sample5))
print(find_entities_with_prefixes(sample6))

print(find_entities_with_prefixes(sample7))
print(find_entities_with_prefixes(sample8))
print(find_entities_with_prefixes(sample9))
print(find_entities_with_prefixes(sample10))
print(find_entities_with_prefixes(sample11))
print(find_entities_with_prefixes(sample12))
print(find_phone_number_in_text(sample13))
print(find_phone_number_in_text(sample14))
print(find_phone_number_in_text(sample15))
print(find_phone_number_in_text(sample16))


# sample1 = "Aadhar : 453565248546\n"
# print("\n\n\n\n\n")
# print(find_labelled_info_in_text(sample1))
