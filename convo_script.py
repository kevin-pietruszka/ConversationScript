# 3rd party libraries
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from chromedriver_py import binary_path 
from service import Service
import traceback


#TODO  Change which link you are 
is_nav = True

# data files
import excel_reader as er
from nav_ids import *
from general_ids import *


# global vars and constants
previous = None
EXTIME = 3
nav_link = 'https://gatech.co1.qualtrics.com/jfe/form/SV_4U8wGXJRFOMekfk' # NAV/BSH
east_link = "https://gatech.co1.qualtrics.com/jfe/form/SV_72O9mThAOKPFYeq" # east campus

link = None
if is_nav:
    link = nav_link
else:
    link = east_link

def next_page():
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
            next_page()

            ra = wait_click(ras[resident['ra_name']])

            if is_nav:
                next_page()

            res_name = wait_type(ids['resident'], resident['name'])
            b = wait_click(buildings[resident['building']])
            next_page()

            f = wait_click(floors[resident['building'] + resident['floor']])
            next_page()

            
            r = wait_click(rooms[resident['building'] + resident['apartment/room']])
            l = wait_click(letters[resident['bedroom']])
            d = wait_type(ids['date'], resident['date'])

            meth = wait_click(methods[str(resident['method'])])

            topic = wait_click(topics[str(resident['topic'])])

            next_page()

            if resident['topic'] == 7: 
                purpose = wait_click(purposes[str(resident['purpose'])])

            desc = wait_type(ids['description'], resident['description'])
            
            next_page()

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