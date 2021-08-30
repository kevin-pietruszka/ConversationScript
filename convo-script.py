
from typing import final
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Use RA_NAME, RA_EMAIL, 
import excel_reader

browser = Chrome()
browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')


def nextPage():

    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "NextButton")))
    next_button.click()

<<<<<<< HEAD

=======
try:
>>>>>>> fe9ef5fceffa73b80f43e19a2ea058c37c47c5b8

def main():

    try:

        time.sleep(2)

        # Select community
        # NAVW: QR~QID36~11
        # NAVS: QR~QID36~12
        # NAVE: QR~QID36~13
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
        building = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID36~17")))
        building.click()

        time.sleep(0.5)
        nextPage()
        # NAW: QR~QID36~11
        # NAS: QR~QID36~12
        # NAE: QR~QID36~13
        # BSH: QR~QID36~17
        #TODO logic to decide building selection
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID36~17")))
        element.click()

        #floor
        options = browser.find_elements_by_tag_name("option")
        for opt in options:
            #TODO replace with excel data
            if opt.text == "1":
                opt.click()

        time.sleep(0.5)
        nextPage()

        #room number 
        li = browser.find_elements_by_tag_name("li")

        time.sleep(5)

    finally:
        browser.quit()

if __name__ == "__main__":
    main()