from curses.ascii import DEL
from email.policy import default
from imp import IMP_HOOK
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
##from chromedriver_py import binary_path 
from service import Service
import traceback
import json

ids = {
    
    "ra":"QR~QID45",
    "ra_email": "QR~QID38",
    "resident":"QR~QID2",
    "building":"QR~QID39",
    "floor":"QR~QID58",
    "bedroom":"QR~QID91",
    "date":"QR~QID3",
    "description":"QR~QID49",
    "calendar":"QID3_cal"
}



# service_object = Service(binary_path)
# browser = webdriver.Chrome(executable_path=binary_path)

import chromedriver_binary
browser = webdriver.Chrome()

#Change this if connection is slow
EXTIME = 10
previous = None
previous_option = None

link = 'https://gatech.co1.qualtrics.com/jfe/form/SV_3R8ddlzjI7zwGEe'


def nextPage():
    next_button = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.NAME, "NextButton")))
    next_button.click()
    wait_for_page()

def backPage():
    back_button = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.NAME, "PreviousButton")))
    back_button.click()
    wait_for_page()


def id_click(toClick):
    global previous 
    temp = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, toClick)))
    temp.click()
    previous = temp

def id_type(toTypeTo, message):
    global previous
    temp = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, toTypeTo)))
    temp.send_keys(message)
    previous = temp

def arb(dict):
    # print(next(iter(dict.items())))
    return next(iter(dict.values()))

def wait_stale():
    global previous
    return WebDriverWait(browser, EXTIME).until(EC.staleness_of(previous))

def wait_for_page():

    # WebDriverWait(browser, EXTIME).until(EC.presence_of_element_located((By.NAME, "NextButton")))
    # WebDriverWait(browser, EXTIME).until(EC.presence_of_element_located((By.NAME, "PreviousButton")))
    body = WebDriverWait(browser, EXTIME).until(EC.visibility_of_all_elements_located((By.ID, "SurveyEngineBody")))


def list_options(tag):
    global previous_option 
    if previous_option is not None:
        WebDriverWait(browser, EXTIME).until(EC.staleness_of(previous_option))
    WebDriverWait(browser, EXTIME).until(EC.presence_of_all_elements_located((By.TAG_NAME, tag)))
    options = browser.find_elements_by_tag_name(tag)

    #print("inputs, ", options)   
    print(len(options), options[0])
    
    previous_option = options[0]

    out = {}
    for opt in options:

        kevin = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', opt)
        temp = str(kevin.get('id'))
        
        opt_text = opt.text
        if temp != 'None' and opt_text != "":
            out[opt_text] = temp

    print(out)
    print("")
    
    return out

def find_rooms(building):

    out = {}
    WebDriverWait(browser, EXTIME).until(EC.presence_of_all_elements_located((By.TAG_NAME, "span")))
    WebDriverWait(browser, EXTIME).until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    room_nums = browser.find_elements_by_xpath("//li/span/label/span")
    inputs = browser.find_elements_by_xpath("//li/input")


    for i in range(len(inputs)):

        kevin = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', inputs[i])
        temp = str(kevin.get('id'))
        out[building+room_nums[i].text] = temp

    print(out)
    print("")

    return out




def get_ids():

    browser.get(link)
    wait_for_page()

    all_areas = list_options("option")
    all_ras = {}
    all_buildings = {}
    all_floors = {}
    all_rooms = {}

    for area, area_id in all_areas.items():
        
        # Select community
        id_click(area_id)
        nextPage()
        
        #ra name
        wait_stale()
        ra_ids = list_options("option")
        all_ras.update(ra_ids)

        id_click(arb(ra_ids))
        nextPage()

        id_type(ids["resident"], "test")
        buildings_ids = list_options("option")
        all_buildings.update(buildings_ids)
        
        for building, build_id in buildings_ids.items():

            id_click(build_id)
            nextPage()

            # wait_class("option")
            wait_stale()
            floor_ids = list_options("option")
            updated_floor = {}
            for floor in floor_ids.keys():
                updated_floor[building+floor] = floor_ids[floor] 

            all_floors.update(updated_floor) 
            
            for floor in updated_floor.values():

                wait_stale()
                id_click(floor)
                nextPage()
                wait_stale()
                rooms = find_rooms(building)
                all_rooms.update(rooms)
                backPage()

            backPage()

        # print(all_floor_ids)
        backPage()
        backPage()
    
    with open('NAVids.py', 'w') as convert_file:
        convert_file.write("areas = ")
        convert_file.write(json.dumps(all_areas))
        convert_file.write("\nras = ")
        convert_file.write(json.dumps(all_ras))
        convert_file.write("\nbuildings = ")
        convert_file.write(json.dumps(all_buildings))
        convert_file.write("\nfloors = ")
        convert_file.write(json.dumps(all_floors))
        convert_file.write("\nrooms = ")
        convert_file.write(json.dumps(all_rooms))



def main():
    try:
        get_ids()

    except Exception as e:

        print(traceback.format_exc())
        browser.quit()



if __name__ == "__main__":
    main()
    browser.quit()
    # test = {
    #     "kevin": 3,
    #     "brett": 1
    # }
    # with open('allids.py', 'w') as convert_file:
    #     convert_file.write("areas = ")
    #     convert_file.write(json.dumps(test))