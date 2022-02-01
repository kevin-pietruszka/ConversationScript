from asyncio import sleep
from curses.ascii import DEL
from distutils.command.build import build
from email.policy import default
from imp import IMP_HOOK
from math import floor
from multiprocessing.connection import wait
from os import preadv
from turtle import back, delay
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from chromedriver_py import binary_path 
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



service_object = Service(binary_path)
browser = webdriver.Chrome(executable_path=binary_path)

#Change this if connection is slow
EXTIME = 10
previous = None


link = "https://gatech.co1.qualtrics.com/jfe/form/SV_72O9mThAOKPFYeq"


def nextPage():
    
    next_button = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.NAME, "NextButton")))
    # WebDriverWait(browser, EXTIME).until(EC.staleness_of(next_button))
    next_button.click()
    wait_for_page()

def backPage():
    back_button = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.NAME, "PreviousButton")))
    # WebDriverWait(browser, EXTIME).until(EC.staleness_of(back_button))
    back_button.click()
    wait_for_page()


def id_click(toClick):
    global previous 
    temp = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, toClick)))
    # WebDriverWait(browser, EXTIME).until(EC.staleness_of(temp))
    temp.click()
    previous = temp

def id_type(toTypeTo, message):
    global previous
    temp = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, toTypeTo)))
    # WebDriverWait(browser, EXTIME).until(EC.staleness_of(temp))
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

    WebDriverWait(browser, EXTIME).until(EC.presence_of_all_elements_located((By.TAG_NAME, tag)))
    options = browser.find_elements_by_tag_name(tag)
    out = {}
    for opt in options:
        
        kevin = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', opt)
        temp = str(kevin.get('id'))
        if temp != 'None' and opt.text != "":
            out[opt.text] = temp

    # print(out)
    # print("")
    
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

    # print(out)
    # print("")

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
        page_ids = list_options("option")
        # separate building ids

        buildings_ids = {}
        ra_ids = {}

        for key, val in page_ids.items():
            if len(key) == 3:
                buildings_ids[key] = val
            else:
                ra_ids[key] = val


        all_ras.update(ra_ids)
        all_buildings.update(buildings_ids)

        backPage()


    id_click(arb(all_areas))
    nextPage()

    id_click(all_ras["Will Ponder"])
    id_type(ids["resident"], "test")
    


    for building, build_id in all_buildings.items():

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

        
    
    with open('HHCids.py', 'w') as convert_file:
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