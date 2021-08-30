import datetime
import xlrd2 as xlrd

# Function to read an excel sheet and assign variables for script
loc = "~/Documents/Convo-Logs-Brett.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
count = 0


# Starts row 0 col 0: so subtract 1 from each
RESDIENTS = [] # A double array full of all info needed for script
for i in range(1, sheet.nrows):
    resident_i = {}

    resident_i["RA_Name"] = sheet.cell_value(i, 0)
    resident_i["RA_Email"] = sheet.cell_value(i, 1)
    resident_i["Name"] = sheet.cell_value(i, 2)
    resident_i["Building"] = sheet.cell_value(i, 3)
    resident_i["Floor"] = int(sheet.cell_value(i, 4))
    resident_i["Apartment/Room"] = int(sheet.cell_value(i, 5))
    resident_i["Bedroom"] = sheet.cell_value(i, 6)
    a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(i, 7), wb.datemode))
    date = str(a1_as_datetime).split(" ")[0]
    resident_i["Date"] = date[5:7] + "/" +date[8:] + "/" + date[0:4]
    resident_i["Method"] = int(sheet.cell_value(i, 8))
    resident_i["Topic"] = int(sheet.cell_value(i, 9))

    RESDIENTS.append(resident_i)


"""
for res in RESDIENTS:
    print(res)
    print()
"""


