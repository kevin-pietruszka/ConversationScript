from time import sleep
import pickle
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

PREVIOUS = None
EXTIME = 2
NEXT = "NextButton"
BACK = "PreviousButton"
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver',options=options)


# Page status and changing pages

def get_page_status():
    tmp = WebDriverWait(browser, EXTIME).until(EC.visibility_of_all_elements_located((By.XPATH, "//div/form")))
    ele = tmp[0]
    ds = ele.get_property('dataset')
    out = ds['testid']
    return out

def wait_for_page():
    while True:
        #sometimes the connection is too fast or the asynchronous nature causes stale element reference
        try:
            status = get_page_status()
            if status == 'page-ready':
                break
        except:
            pass
        
        sleep(0.02)
    
def change_page(button):
    wait_click(button)
    wait_for_page()


# Reading Elements from the screen

# def wait_for_elements(tag):
#     WebDriverWait(browser, EXTIME).until(EC.visibility_of_all_elements_located((By.TAG_NAME, tag)))

def get_options():

    # Find option elements under select statement
    options = browser.find_elements(By.XPATH, "//select/option")
    
    #Build dictionaries
    out = {}
    example = None
    for ele in options[1:]:
        out[ele.text] = ele.get_attribute("id")
        example = ele.get_attribute("id")

    return out, example

def get_labels():

    labels = browser.find_elements(By.XPATH, "//span/label")

    out = {}
    example = None
    for ele in labels[1:]:
        out[ele.text] = ele.get_attribute("id")
        example = ele.get_attribute("id")

    return out, example

def get_input(name):

    input = browser.find_element(By.XPATH, "//input")
    out = {name: input.get_attribute("id")}

    return out, out[name]


# Interaction with the page

def wait_click(element_id):
    WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, element_id))).click()

def wait_keys(element_id, message):
    WebDriverWait(browser, EXTIME).until(EC.visibility_of_element_located((By.ID, element_id))).send_keys(message)
