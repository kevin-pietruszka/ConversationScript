from HHCids import *
import json

new_dict = {}
for room_num, id in rooms.items():

    temp = id[3:] + "~label"
    new_dict[room_num] = temp.replace("~", "-")


with open('HHCids.py', 'w') as convert_file:
        convert_file.write("\nrooms = ")
        convert_file.write(json.dumps(new_dict))