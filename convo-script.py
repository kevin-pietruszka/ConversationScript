from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from imp import IMP_HOOK
<<<<<<< HEAD
=======
from math import floor
#from os import preadv
#from turtle import back, delay
>>>>>>> 542cf52107b21872c0f1c9828ac70921bf23e50d
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
link = 'https://gatech.co1.qualtrics.com/jfe/form/SV_4U8wGXJRFOMekfk' # NAV/BSH
# link = "https://gatech.co1.qualtrics.com/jfe/form/SV_72O9mThAOKPFYeq" # east campus


def select_communication(resident):
    
    meth = wait_click(areas[str(resident['method'])])

    topic = wait_click(areas[str(resident['topic'])])

    nextPage()

    if resident['topic'] == 7: 
        purpose = wait_click(areas[str(resident['purpose'])])

    desc = wait_type(ids['description'], resident['description'])

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
            break

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

            meth = wait_click(methods[str(resident['method'])])

            topic = wait_click(topics[str(resident['topic'])])

            nextPage()

            if resident['topic'] == 7: 
                purpose = wait_click(purposes[str(resident['purpose'])])

            desc = wait_type(ids['description'], resident['description'])
            
            nextPage()

            """
            inperson = wait_click("QID48-1-label")

            gettoknow = wait_click("QID41-1-label")

            nextPage()

            wait_type(ids['description'], resident['description'])
            """

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