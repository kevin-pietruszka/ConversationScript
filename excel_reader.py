import datetime
import xlrd2 as xlrd

# Function to read an excel sheet and assign variables for script
# TODO
loc = "2336-Convo-Logs.xlsx"
#loc = "~/Downloads/Reese.xlsx"
#loc = "conversationsmaelynn.xlsx"
#loc = "~/Downloads/7th-Convo-Logs.xlsx"

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
        resident_i["ra_email"] = ""

    resident_name = sheet.cell_value(i, 2)

    if resident_name == "": # Allows for empty rooms
        continue

    resident_i["name"] = resident_name
    resident_i["building"] = sheet.cell_value(i, 3)

    if resident_i["building"] in ["BRN", "SMT", "HRS"]:
        resident_i["area"] = "BSH"
    elif resident_i["building"] in ["NAW", "NAN"]:
        resident_i["area"] = "NANW"
    else:
        resident_i["area"] = sheet.cell_value(i, 3)

    resident_i["floor"] = str(int(sheet.cell_value(i, 4)))
    resident_i["apartment/room"] = str(int(sheet.cell_value(i, 5)))
    resident_i["bedroom"] = sheet.cell_value(i, 6).upper()
    #print(sheet.cell_value(i, 7), wb.datemode)
    a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(i, 7), wb.datemode))
    date = str(a1_as_datetime).split(" ")[0]
    resident_i["date"] = date[5:7] + "-" +date[8:] + "-" + date[0:4]

    resident_i["method"] = int(sheet.cell_value(i, 8))
    resident_i["topic"] = int(sheet.cell_value(i, 9))
    resident_i["purpose"] = sheet.cell_value(i, 10)
    if resident_i["purpose"] == "":
        resident_i["purpose"] = 0
    else:
        resident_i["purpose"] = int(resident_i["purpose"])
    resident_i["description"] = str(sheet.cell_value(i, 11))

    RESDIENTS.append(resident_i)


if __name__ == "__main__":
    for res in RESDIENTS:
        print(res)
        print()