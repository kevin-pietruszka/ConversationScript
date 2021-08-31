
from typing import final
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Use RA_NAME, RA_EMAIL, 
#import excel_reader

browser = Chrome()
browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')

ids = {
    "NAW": "QR~QID36~11",
    "NAS": "QR~QID36~12",
    "NAE": "QR~QID36~13",
    "BSH": "QR~QID36~17",
    "ra":"QR~QID45",
    "resident":"QR~QID2",
    "building":"QR~QID39",
    "foor":"QR~QID58",
    "letter":"QR~QID91",
    "date":"QR~QID3"
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

    try:

        time.sleep(2)

        # Select community
        # NAW: QR~QID36~11
        # NAS: QR~QID36~12
        # NAE: QR~QID36~13
        # BSH: QR~QID36~17
        #TODO
        area = wait(ids["BSH"])
        area.click()

        nextPage()
        
        #ra name
        wait(ids["ra"])
        parse_options("option", "Kevin Pietruszka")

        nextPage()

        #residents name
        residents_name = wait(ids["resident"])
        residents_name.send_keys("Brian Youn")

        #building
        wait(ids["building"])
        parse_options("option", "BRN")

        nextPage()

        #floor
        wait(ids["foor"])
        parse_options("option", "1")

        nextPage()

        #room number and etter
        wait(ids["letter"])
        parse_options("label", "112")
        parse_options("option", "A")

        #date
        date = wait(ids["date"])
        date.send_keys("08-31-2021")

        #contact type
        parse_options("label", "In person")

        #topic
        parse_options("label", "Social Get to Know")

        time.sleep(5)

    finally:
        browser.quit()

if __name__ == "__main__":
    main()