import fitz
import re
import time

# Flags
email = 1
ifsc= 1
accno= 1
cardno= 1
phoneno= 1
panno= 1
name= 1
pin = 1
city = 1

black_bar = 1
dashed_accno = 0

check_inside = 0

class Redactor:

    # static methods work independent of class object
    @staticmethod
    def get_sensitive_data(lines):
        """ Function to get all the lines """
        special_acc_no = []

        # ESSENTIALS
        EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
        IFSC_REG = r"([A-Z]{4}0[A-Z0-9]{6})"
        ACC_REG = r"(0*[0-9]{9,18})"
        CARD_REG = r"([0-9]{4}[\s\-][0-9]{4}[\s\-][0-9]{4}[\s\-][0-9]{4})"
        PAN_REG = r"([A-Z]{4}(A|B|C|F|G|H|L|J|P|T){1}[0-9]{4}[A-Z]{1})"
        NAME_MR_MS = r"(^[M|m][r|R|s|S][.\s]*\w+\s\w+\s?\w+)"


        # TAGGED REGEXES
        ACC_TAG = r"Account\s?(Number)?(no)?\.?\s?\:?\s?([0-9]{9,18})"
        ACC_DASH = r"Account\s?(Number)?(no)?\.?\s?\:?\s?(\w+\-\s?\w+\-\w+)"
        NAME_TAG = r"Name\s?\:?\s?(\w+[^\S\r\n]+(\w+)?)"
        CITY_TAG = r"City\s?\:?\s?(\w+)"
        PIN_TAG = r"Pin\s?\:?\s?(\w+)"

        total_changes = 0
        c_email = re.compile(EMAIL_REG, re.IGNORECASE)
        c_ifsc = re.compile(IFSC_REG, re.IGNORECASE)
        c_card = re.compile(CARD_REG, re.IGNORECASE)
        c_pan = re.compile(PAN_REG, re.IGNORECASE)
        c_name_mr_ms = re.compile(NAME_MR_MS, re.IGNORECASE)
        c_acc = re.compile(ACC_TAG, re.IGNORECASE)
        c_acc_dash = re.compile(ACC_DASH, re.IGNORECASE)
        c_name = re.compile(NAME_TAG, re.IGNORECASE)
        c_pin = re.compile(PIN_TAG, re.IGNORECASE)
        c_city = re.compile(CITY_TAG, re.IGNORECASE)
        c_acc_like = re.compile(ACC_REG, re.IGNORECASE)

        for line in lines:
            redacted_in_line = []

            search = c_email.search(line)
            if search and email == 1:
                total_changes += 1
                yield search.group(1)

            search = c_acc_like.search(line)
            if search and accno == 1:

                if search.group(1) not in redacted_in_line:
                    redacted_in_line.append(search.group(1))
                    yield search.group(1)
                    total_changes += 1

            search = c_ifsc.search(line)
            if search and ifsc == 1:
                total_changes += 1
                yield search.group(1)

            search = c_card.search(line)
            if search and cardno == 1:
                total_changes += 1
                if search.group(1) not in redacted_in_line:
                    redacted_in_line.append(search.group(1))
                    yield search.group(1)

            search = c_acc.search(line)
            if search and accno == 1:
                total_changes += 1
                if search.group(3) not in redacted_in_line:
                    redacted_in_line.append(search.group(1))
                    yield search.group(3)

            search = c_pan.search(line)
            if search and panno == 1:
                total_changes += 1
                yield search.group(1)

            if c_name_mr_ms.search(line) and name == 1:
                search = c_name_mr_ms.search(line)
                total_changes += 1
                yield search.group(1)

            if c_name.search(line) and name == 1:
                search = c_name.search(line)
                total_changes += 1
                yield search.group(1)
            #
            search = c_acc_dash.search(line)
            if search and dashed_accno == 1:
                special_acc_no.append(search.group(3))
                for x in special_acc_no:
                    c_dashed_acc = re.compile(x)
                    search = c_dashed_acc.search(line)

                    if search :
                        total_changes += 1
                        if search.group() not in redacted_in_line:
                            redacted_in_line.append(search.group())
                            yield search.group()


            search = c_pin.search(line)
            if search and pin == 1:
                total_changes += 1
                if search.group(1) not in redacted_in_line:
                    redacted_in_line.append(search.group(1))
                    yield search.group(1)

            search = c_city.search(line)

            if search and city == 1:
                total_changes += 1
                if search.group(1) not in redacted_in_line:
                    redacted_in_line.append(search.group(1))
                    yield search.group(1)



    # constructor
    def __init__(self, path):
        self.path = path

    def redaction(self):

        """ main redactor code """

        # opening the pdf
        doc = fitz.open(self.path)
        total_redactions = 0
        # iterating through pages
        for page in doc:
            # print(page.get_fonts())

            # _wrapContents is needed for fixing
            # alignment issues with rect boxes in some
            # cases where there is alignment issue
            page.wrap_contents()


            # getting the rect boxes which consists the matching email regex
            sensitive = self.get_sensitive_data(page.get_text("text")
                                                .split('\n'))

            for data in sensitive:
                areas = page.search_for(data)
                # drawing outline over sensitive datas
                total_redactions += len(areas)
                if black_bar != 0:
                    [page.add_redact_annot(area, fill=(0, 0, 0)) for area in areas]
                else:
                    [page.add_redact_annot(area, text="X" * len(data), fill=(1, 1, 1)) for area in areas]

            # applying the redaction
            page.apply_redactions()

        print("SUCCESSFULLY REDACTED THE FILE  : ", str(path))
        # saving it to a new pdf
        if black_bar != 0:
            doc.save(path[:-4] + '-redacted_black_timed.pdf')
            print("\nSAVED FILE PATH : ",str(path[:-4] + "-redacted_black_timed.pdf"))

        else:
            doc.save(path[:-4] + '-redacted_mask_timed.pdf')
            print("\nSAVED FILE PATH : ", str(path[:-4] + "-redacted_black_timed.pdf"))

        print("\nTOTAL REDACTIONS DONE IS : ", total_redactions)



# driver code for testing
if __name__ == "__main__":
    # replace it with name of the pdf file

    path = input("Enter a valid path : ")
    redactor = Redactor(path)
    start_time = time.time()
    print("--------------------------------REPORT-----------------------------------")
    redactor.redaction()
    end_time = time.time()
    print("\nTotal runtime of redaction using MUPDF is : {}".format(end_time-start_time))
