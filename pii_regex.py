import re


def find_entities_with_prefixes(s):
    list_of_entities = []
    # FINDING all the occurrences where the prefix is in the form of Mr./MR./Mr /MR/Ms./MS>/Ms/MS /
    regex1 = 'M[r|R|s|S][.\s]*\w+\s\w+\s?\w+'
    p1 = re.compile(regex1)
    list_of_entities = re.findall(p1, s)

    # FINDING all the occurrences where the prefix is in the form of Mrs./MRS./Mrs /MRS /
    regex1 = 'M[R|r][S|s][.\s]*\w+\s\w+\s?\w+'
    p2 = re.compile(regex1)
    list_of_entities.extend(re.findall(p2, s))

    return list_of_entities

def find_phone_number_in_text(s):
    list_of_ph_nos = []
    regex1 = "\+?[0-9]{0,2}\s*[0-9]{5}\s?[0-9]{5}"
    p1 = re.compile(regex1)
    list_of_ph_nos.extend(re.findall(p1, s))

    ph_nos_list = [x.strip() for x in list_of_ph_nos]

    return ph_nos_list

def find_labelled_info_in_text(s):
    regex = '\w+(\s?):(\s?)\w+'
    p = re.compile(regex)
    list_of_labelled_info = re.findall(p, s).split()
    dict_of_info = dict()
    for info in list_of_labelled_info:
        idx = s.find(':')
        label = info[:idx]
        value = info[idx+1:]
        dict_of_info[label] = value
    if (s == None):
        return None
    if dict_of_info is not None:
        return dict_of_info
    else:
        return None
def find_pan_in_text(s):
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"

    p = re.compile(regex)

    if (s == None):
        return None

    if (re.findall(p, s)):
        return (re.findall(p, s))
    else:
        return None


def find_aadhar_in_text(s):
    regex1 = ("[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}")
    regex2 = ("[2-9]{1}[0-9]{11}")
    regex3 = ("[2-9]{1}[0-9]{3}[-~][0-9]{4}[-~][0-9]{4}")

    p1 = re.compile(regex1)
    p2 = re.compile(regex2)
    p3 = re.compile(regex3)

    list_of_all_aadhars = []
    if (s == None):
        return None

    aadhar_nos_list1 = re.findall(p1, s)
    aadhar_nos_list2 = re.findall(p2, s)
    aadhar_nos_list3 = re.findall(p3, s)

    if (len(aadhar_nos_list1) == 0 and len(aadhar_nos_list2) == 0 and len(aadhar_nos_list3) == 0):
        return None
    else:
        if aadhar_nos_list1 is not None:
            list_of_all_aadhars.extend(aadhar_nos_list1)
        if aadhar_nos_list2 is not None:
            list_of_all_aadhars.extend(aadhar_nos_list2)
        if aadhar_nos_list3 is not None:
            list_of_all_aadhars.extend(aadhar_nos_list3)
        return list_of_all_aadhars



def find_ifsc_in_text(s):
    regex = "[A-Z]{4}0[A-Z0-9]{6}"

    p = re.compile(regex)
    if (s == None):
        return None

    if (re.findall(p, s)):
        return (re.findall(p, s))
    else:
        return None


def find_acc_no_in_text(s):
    regex = "0*[0-9]{9,18}"

    p = re.compile(regex)
    if (s == None):
        return None
    list_of_acc_nos = re.findall(p, s)
    list_of_aadhar_nos = find_aadhar_in_text(s)
    acc_no_list = list()
    if (list_of_acc_nos):
        if(list_of_aadhar_nos is not None):
            for acc_no in list_of_acc_nos:
                if acc_no not in list_of_aadhar_nos:
                    acc_no_list.append(acc_no)
            list_of_acc_nos = acc_no_list
        return list_of_acc_nos
    else:
        return None


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
