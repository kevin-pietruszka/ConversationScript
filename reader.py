import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# import excel_reader as er

from ids import *

browser = Chrome()


def nextPage():
    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "NextButton")))
    next_button.click()

def backPage():
    back_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "PreviousButton")))
    back_button.submit()
    

def wait(id):

    return WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, id)))

def list_options(tag):

    options = browser.find_elements_by_tag_name(tag)
    out = None
    for opt in options:
        print(opt.text + ":" + opt.id) 
        out = opt
    return out

def main():

    browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')
    time.sleep(3)


    for area, area_id in areas.items():

        print(area)
        print(area_id)
        
        #try:
        
        # Select community
        a = wait(area_id)
        a.click()

        nextPage()
        
        #ra name
        wait(ids["ra"])
        
        temp = list_options("option")
        temp.click()

        backPage()


if __name__ == "__main__":
    main()