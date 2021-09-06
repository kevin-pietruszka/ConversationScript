
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

browser = Chrome()
browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')


def nextPage():
    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "NextButton")))
    next_button.click()

try:

    # Select community

    # NAW: QR~QID36~11
    # NAS: QR~QID36~12
    # NAE: QR~QID36~13
    # BSH: QR~QID36~17
    #TODO logic to decide building selection
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID36~17")))
    element.click()

    nextPage()
    
    # Find name of person
    name = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID45")))
    options = browser.find_elements_by_tag_name("option")
    for opt in options:
        #TODO replace with excel data
        if opt.text == "Kevin Pietruszka":
            opt.click()

    nextPage()

    residents_name = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID2")))

    residents_name.send_keys("Heil Hydra")

    time.sleep(5)

finally:
    browser.quit()