import datetime
import xlrd2 as xlrd

loc = "~/Downloads/MasterConvoSheet.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
count = 0

data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))

command_lines = []
with open("log.txt", "r") as a_file:
    for line in a_file:
        stripped_line = line.strip()
        command_lines.append(stripped_line)

a1_as_datetime = datetime.datetime(*xlrd.xldate_as_tuple(date, wb.datemode))
date = str(a1_as_datetime).split(" ")[0]