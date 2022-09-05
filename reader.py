from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver',options=options)
PREVIOUS = None
EXTIME = 10
NEXT = "NextButton"
BACK = "PreviousButton"
link = "https://gatech.co1.qualtrics.com/jfe/form/SV_3wMI1pXNJOwLJL8"

def get_page_status():
    tmp = WebDriverWait(browser, EXTIME).until(EC.visibility_of_all_elements_located((By.XPATH, "//div/form"))).get_property('dataset')
    return tmp['testid']

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
        

def wait_for_elements(tag):
    WebDriverWait(browser, EXTIME).until(EC.visibility_of_all_elements_located((By.TAG_NAME, tag)))

def wait_click(element_id):
    WebDriverWait(browser, EXTIME).until(EC.element_to_be_clickable((By.ID, element_id))).click()

def wait_keys(element_id, message):
    WebDriverWait(browser, EXTIME).until(EC.visibility_of_element_located((By.ID, element_id))).send_keys(message)

def change_page(button):
    wait_click(button)
    wait_for_page()


def get_options():

    #wait for page elements to load in DOM
    wait_for_elements("option")

    # Find option elements under select statement
    options = browser.find_elements(By.XPATH, "//select/option")
    
    #Build dictionaries
    out = {}
    for ele in options[1:]:
        out[ele.text] = ele.get_attribute("id")
        example = ele.get_attribute("id")

    return out, example

def get_input(name):

    wait_for_elements("input")
    input = browser.find_element(By.XPATH, "//input")
    out = {name: input.get_attribute("id")}

    return out, out[name]

def main():
    
    browser.get(link)
    
    # Get the community names and IDs 
    resident_communities, one = get_options()
    wait_click(one)

    change_page(NEXT)

    # Get RA names and IDs
    RAs, one = get_options()

    change_page(NEXT)

    resident_name, one = get_input("resident_name")
    wait_keys(one, "Brett")

    tmp, one = get_options()
    buildings = {}
    for building, id in tmp.items():
        buildings[building[0:3]] = id
    wait_click(one)

    floors = {}
    rooms = {}

    for building, building_id in buildings.items():

        wait_click(building_id)
        change_page(NEXT)
        # Grab floor ids
        building_floors, _ = get_options()

        for floor_num, floor_id in building_floors.items():

            floors[building + floor_num] = floor_id
            wait_click(floor_id)
            change_page(NEXT)
            # Grab room numbers
            room_numbers, _ = get_options()
            for key, val in room_numbers.items():
                if len(key) > 1:
                    rooms[building + key] = val
            change_page(BACK)
        
        change_page(BACK)
        print(floors)
        print(rooms)

    print(floors)
    print(rooms)

if __name__ == "__main__":
    try:
        main()
    finally:
        browser.close()