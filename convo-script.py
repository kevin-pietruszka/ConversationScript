
import re
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

browser = Chrome()


ids = {
    "NAW": "QR~QID36~11",
    "NAS": "QR~QID36~12",
    "NAE": "QR~QID36~13",
    "BSH": "QR~QID36~17",
    "ra":"QR~QID45",
    "resident":"QR~QID2",
    "building":"QR~QID39",
    "foor":"QR~QID58",
    "bedroom":"QR~QID91",
    "date":"QR~QID3",
    "description":"QR~QID49",
    "calendar":"QID3_cal"
}


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

    failed = []
    fail = 0
    for resident in er.RESDIENTS:
        print(resident)
        try:
            
            browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')
            time.sleep(3)

            # Select community
            area = wait(ids[resident["area"]])
            area.click()

            nextPage()
            
            #ra name
            wait(ids["ra"])
            parse_options("option", resident["ra_name"])

            nextPage()

            #residents name
            residents_name = wait(ids["resident"])
            residents_name.send_keys(resident["name"])

            #building
            wait(ids["building"])
            parse_options("option", resident["building"])

            nextPage()

            #floor
            wait(ids["foor"])
            parse_options("option", resident["floor"])

            nextPage()

            #room number and letter
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

            nextPage()

            desc = wait(ids["description"])
            desc.send_keys(resident["description"])

            nextPage()
            
            time.sleep(5)

        except:
            
            failed.append(resident["name"])
            fail+=1
            
    print("This many entries failed, " + str(fail))
    print(failed)
    browser.quit()

if __name__ == "__main__":
    main()