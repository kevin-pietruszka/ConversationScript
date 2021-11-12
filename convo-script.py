from typing import final
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Use RA_NAME, RA_EMAIL, 
import excel_reader as er
from ids import *

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

    for opt in options:
        if opt.text == key:
            opt.click()


def main():

    browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')
    time.sleep(3)

    browser.maximize_window()

    for resident in er.RESDIENTS:
        print(resident)
        #try:
        
        # Select community
        area = wait(areas[resident["area"]])
        area.click()

        nextPage()
        
        #ra name
        ra = wait(RAs[resident["ra_name"]])
        ra.click()

        #ra email
        ra_email = wait(ids["ra_email"])
        if resident["ra_email"] == None:
            pass
        else:
            ra_email.send_keys(resident["ra_email"])

        time.sleep(1)
        nextPage()
        time.sleep(1)

        #residents name
        residents_name = wait(ids["resident"])
        residents_name.send_keys(resident["name"])

        #building
        b = wait(buildings[resident["building"]])
        b.click()

        time.sleep(1)
        nextPage()
        time.sleep(1)

        #floor
        f = wait(floors[resident["floor"]])
        f.click()

        time.sleep(1)
        nextPage()
        time.sleep(1)

        #room number and letter
        time.sleep(3)
        date = wait(ids["date"])
        date.send_keys(resident["date"])
        room = wait(rooms[resident["building"] + resident["apartment/room"]])
        room.click()
        letter = wait(letters[resident["bedroom"]])
        letter.click()

        #contact type
        # TODO
        # parse_options("label", "In person")
        inperson = wait("QID48-1-label")
        inperson.click()

        #topic
        # TODO
        # parse_options("label", "Social/Get-to-know")
        gettoknow = wait("QID41-1-label")
        gettoknow.click()

        time.sleep(1)
        nextPage()
        time.sleep(1)

        desc = wait(ids["description"])
        desc.send_keys(resident["description"])

        time.sleep(1)
        nextPage()
        time.sleep(5)

if __name__ == "__main__":
    main()