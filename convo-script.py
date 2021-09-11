
import re
from typing import final
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Use RESIDENTS 

import excel_reader

# Use RA_NAME, RA_EMAIL, 
import excel_reader as er

from dictionary import *

browser = Chrome()





def nextPage():
    #TODO Find better way to wait for next button. It has error occaisionaly
    time.sleep(0.5)
    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "NextButton")))
    next_button.click()

def wait(id):

    return WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, id)))
    
def parse_options(tag, key):

    options = browser.find_elements_by_tag_name(tag)

import excel_reader as er

browser = Chrome()


ids = {
    "NAW": "QR~QID36~11",
    "NAS": "QR~QID36~12",
    "NAE": "QR~QID36~13",
    "BSH": "QR~QID36~17",
    "ra":"QR~QID45",
    "ra_email": "QR~QID38",
    "resident":"QR~QID2",
    "building":"QR~QID39",
    "floor":"QR~QID77", #Kev had 58, its different for each building SMT 95
    "bedroom":"QR~QID91",
    "date":"QR~QID3",
    "description":"QR~QID49",
    "calendar":"QID3_cal"
}


def nextPage():
    #TODO Find better way to wait for next button. It has error occaisionaly 
    time.sleep(0.75)
    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "NextButton")))
    next_button.click()
    

def wait(id):

    return WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, id)))
    
def parse_options(tag, key):

    options = browser.find_elements_by_tag_name(tag)

    for opt in options:
        if opt.text == key:
            opt.click()
    
    #print()

failed = []
fail = 0

def main():

<<<<<<< HEAD
    failed = []
    fail = 0

    browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')
    time.sleep(3)

    browser.maximize_window()

    for resident in er.RESDIENTS:
        print(resident)
        #try:
        
        browser.refresh()
        time.sleep(5)
        
        
        # Select community
        area = wait(ids[resident["area"]])
        area.click()
=======
    global fail, failed

    browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')
    
    for resident in er.RESDIENTS:
        #print(resident)
        try:
            
            time.sleep(3)
>>>>>>> 3bfef124434c9239b5aa494d144c71184683861b

        nextPage()
        
        #ra name
        wait(ids["ra"])
        parse_options("option", resident["ra_name"])

        #ra email
        ra_email = wait(ids["ra_email"])
        ra_email.send_keys(resident["ra_email"])


        nextPage()

        #residents name
        residents_name = wait(ids["resident"])
        residents_name.send_keys(resident["name"])

        #building
        wait(ids["building"])
        parse_options("option", resident["building"])

        nextPage()

        #floor
        wait(ids["floor"])
        parse_options("option", resident["floor"])

        nextPage()

        #room number and letter
        time.sleep(3)
        wait(ids["bedroom"])
        date = wait(ids["date"])
        wait("Logo")
        wait(ids["calendar"])
        parse_options("label", resident["apartment/room"])
        parse_options("option", resident["bedroom"])


        #date
        date.send_keys(resident["date"])

        #contact type
        # TODO
        parse_options("label", "In person")

        #topic
        # TODO
        parse_options("label", "Social/Get-to-know")

<<<<<<< HEAD
        nextPage()

        desc = wait(ids["description"])
        desc.send_keys(resident["description"])
=======
            desc = wait(ids["description"])
            desc.send_keys(resident["description"])

            nextPage()

            time.sleep(2)

            browser.refresh()
>>>>>>> 3bfef124434c9239b5aa494d144c71184683861b

        nextPage()
        
        time.sleep(5)
        #browser.quit()
        #time.sleep(5)

            
        """
        except:
<<<<<<< HEAD
            
            failed.append(resident["name"])
            fail+=1
        """
            
    #print("This many entries failed, " + str(fail))
    #print(failed)
    #browser.quit()
=======
            print("Failed on: " + str(resident["name"]))
            time.sleep(10)
            browser.quit()
            return
   
>>>>>>> 3bfef124434c9239b5aa494d144c71184683861b

if __name__ == "__main__":
    main()