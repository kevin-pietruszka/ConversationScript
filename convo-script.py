from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from imp import IMP_HOOK
from selenium import webdriver
from chromedriver_py import binary_path 
from service import Service
import traceback

# Use RA_NAME, RA_EMAIL, 
import excel_reader as er
from NAVids import *
from ids import *

previous = None
EXTIME = 3
link = 'https://gatech.co1.qualtrics.com/jfe/form/SV_4U8wGXJRFOMekfk'
# link = "https://gatech.co1.qualtrics.com/jfe/form/SV_72O9mThAOKPFYeq"

def nextPage():
    next_button = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.NAME, "NextButton")))
    next_button.click()
    wait_for_page()

def wait_for_page():

    body = WebDriverWait(browser, EXTIME).until(EC.visibility_of_all_elements_located((By.ID, "SurveyEngineBody")))
    if previous != None:
        wait_stale()

def wait_stale():
    global previous
    return WebDriverWait(browser, EXTIME).until(EC.staleness_of(previous))

def wait_click(toClick):
    global previous 
    temp = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, toClick)))
    temp.click()
    previous = temp

def wait_type(toTypeTo, message):
    global previous
    temp = WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, toTypeTo)))
    temp.send_keys(message)
    previous = temp


service_object = Service(binary_path)
browser = webdriver.Chrome(executable_path=binary_path)

def main():

    browser.get(link)

    idx = 0

    while True:

        if (idx >= len(er.RESDIENTS)):
            break;

        try:
            wait_for_page()
            resident = er.RESDIENTS[idx]
            print(resident)

            area = wait_click(areas[resident['area']])
            nextPage()

            ra = wait_click(ras[resident['ra_name']])
            nextPage()

            res_name = wait_type(ids['resident'], resident['name'])
            b = wait_click(buildings[resident['building']])
            nextPage()

            f = wait_click(floors[resident['building'] + resident['floor']])
            nextPage()
            
            r = wait_click(rooms[resident['building'] + resident['apartment/room']])
            l = wait_click(letters[resident['bedroom']])
            d = wait_type(ids['date'], resident['date'])

            inperson = wait_click("QID48-1-label")

            gettoknow = wait_click("QID41-1-label")

            nextPage()

            wait_type(ids['description'], resident['description'])

            idx+=1
            
        except:

            print(traceback.format_exc())
            browser.delete_all_cookies()
            browser.get(link)
            print("Retrying")
            browser.quit()

if __name__ == "__main__":
    main()
    browser.quit()