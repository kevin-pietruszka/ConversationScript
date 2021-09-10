
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
    
    #print()


def main():

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

        nextPage()

        desc = wait(ids["description"])
        desc.send_keys(resident["description"])

        nextPage()
        
        time.sleep(5)
        #browser.quit()
        #time.sleep(5)

            
        """
        except:
            
            failed.append(resident["name"])
            fail+=1
        """
            
    #print("This many entries failed, " + str(fail))
    #print(failed)
    #browser.quit()

if __name__ == "__main__":
    main()