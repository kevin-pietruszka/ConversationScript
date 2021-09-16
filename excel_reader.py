import datetime
import xlrd2 as xlrd

# Function to read an excel sheet and assign variables for script
loc = "~/Downloads/MasterConvo.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
count = 0


# Starts row 0 col 0: so subtract 1 from each
RESDIENTS = [] # A array of dictionaries to each conversation
for i in range(1, sheet.nrows):
    resident_i = {}

    name = sheet.cell_value(i, 0)
    if name == "":
        break
    resident_i["ra_name"] = name

    if len(sheet.cell_value(i, 1)) > 0:
        resident_i["ra_email"] = sheet.cell_value(i, 1)
    else:
        resident_i["ra_email"] = None

    resident_i["name"] = sheet.cell_value(i, 2)
    resident_i["building"] = sheet.cell_value(i, 3)

    if resident_i["building"] in ["BRN", "SMT", "HRS"]:
        resident_i["area"] = "BSH"
    else:
        resident_i["area"] = sheet.cell_value(i, 3)

    resident_i["floor"] = str(int(sheet.cell_value(i, 4)))
    resident_i["apartment/room"] = str(int(sheet.cell_value(i, 5)))
    resident_i["bedroom"] = sheet.cell_value(i, 6).upper()
    a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(i, 7), wb.datemode))
    date = str(a1_as_datetime).split(" ")[0]
    resident_i["date"] = date[5:7] + "/" +date[8:] + "/" + date[0:4]

    #resident_i["method"] = int(sheet.cell_value(i, 8))
    #resident_i["topic"] = int(sheet.cell_value(i, 9))
    resident_i["description"] = str(sheet.cell_value(i, 10))

    RESDIENTS.append(resident_i)

"""
for res in RESDIENTS:
    print(res)
    print()
"""