
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


def nextPage():

    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "NextButton")))
    next_button.click()


def main():

    try:

        time.sleep(2)

        # Select community
        # NAW: QR~QID36~11
        # NAS: QR~QID36~12
        # NAE: QR~QID36~13
        # BSH: QR~QID36~17
        #TODO logic to decide building selection
        area = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID36~17")))
        area.click()

        nextPage()
        
        # Find name of person
        name = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID45")))
        options = browser.find_elements_by_tag_name("option")
        for opt in options:
            #TODO replace with excel data
            if opt.text == "Kevin Pietruszka":
                opt.click()

        #TODO Find better way to wait for next button. It has error occaisionaly 
        time.sleep(0.5)
        nextPage()

        # enter residents name
        residents_name = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID2")))
        residents_name.send_keys("Brian Youn")

        #building
        #TODO find ids for the other buildings
        #BRN: QR~QID39~8, SMT: QR~QID39~9, HRS: QR~QID39~9
        #TODO logic to decide building selection
        building = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID39")))
        options = browser.find_elements_by_tag_name("option")
        for opt in options:
            if opt.text == "BRN":
                opt.click()

        time.sleep(0.5)
        nextPage()

        #floor
        building = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID58")))
        options = browser.find_elements_by_tag_name("option")
        for opt in options:
            if opt.text == "1":
                opt.click()

        time.sleep(0.5)
        nextPage()

        #room number
        room_letter = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID91")))
        li = browser.find_elements_by_tag_name("label")
        for l in li:
            if l.text == "112":
                l.click()


        
        
        time.sleep(5)

    finally:
        browser.quit()

if __name__ == "__main__":
    main()