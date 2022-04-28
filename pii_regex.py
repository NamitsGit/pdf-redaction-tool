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
