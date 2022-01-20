from typing import final
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Use RA_NAME, RA_EMAIL, 
import excel_reader as er
from ids import *


def nextPage():
    #TODO Find better way to wait for next button. It has error occaisionaly
    time.sleep(1)
    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "NextButton")))
    next_button.click()
    time.sleep(1)

def backPage():
    #TODO Find better way to wait for next button. It has error occaisionaly
    time.sleep(1)
    next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "PreviousButton")))
    next_button.click()
    time.sleep(1)

def wait(id):

    return WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, id)))

def clearTextBox(textBox):
    if textBox == None:
        return
    try:
        for i in range(200):
            textBox.send_keys(Keys.BACK_SPACE)
    except:
        print("\nDelete TextBox Error (Text Box not None).\n")
    
browser = Chrome()

def main():

    browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')
    #browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_8bG7y2Ts0IHdXCK')
    time.sleep(3)

    idx = 0

    while True:

        if (idx >= len(er.RESDIENTS)):
            break

        try:

            ########## Page 1 ##########
            while True:
                try:
                    resident = er.RESDIENTS[idx]
                    print(resident)
                    #try:
                    
                    # Select community
                    area = wait(areas[resident["area"]])
                    area.click()
                    break
                except Exception as error:
                    print(str(error))
                    #browser.refresh()
                    time.sleep(1)

            nextPage()
            
            ########## Page 2 ##########
            while True:
                try:
                    #ra name
                    ra = wait(RAs[resident["ra_name"]])
                    ra.click()

                    #ra email
                    ra_email = wait(ids["ra_email"])
                    if resident["ra_email"] == None:
                        pass
                    else:
                        ra_email.send_keys(resident["ra_email"])
                    break
                except Exception as error:
                    print(str(error))
                    #browser.refresh()
                    ra_email = wait(ids["ra_email"])
                    clearTextBox(ra_email)
                    time.sleep(1)


            nextPage()

            ########## Page 3 ##########
            while True:
                try:
                    #residents name
                    residents_name = wait(ids["resident"])
                    residents_name.send_keys(resident["name"])

                    #building
                    b = wait(buildings[resident["building"]])
                    b.click()
                    break
                except Exception as error:
                    print(str(error))
                    #browser.refresh()
                    residents_name = wait(ids["resident"])
                    clearTextBox(residents_name)
                    time.sleep(1)

            nextPage()

            ########## Page 4 ##########
            while True:
                try:
                    #floor
                    f = wait(floors[resident["building"] + resident["floor"]])
                    f.click()
                    break
                except Exception as error:
                    print(str(error))
                    #browser.refresh()
                    time.sleep(1)

            nextPage()

            
            ########## Page 5 ##########
            while True:
                try:
                    #room number and letter
                    date = wait(ids["date"])
                    date.send_keys(resident["date"])
                    room = wait(rooms[resident["building"] + resident["apartment/room"]])
                    room.click()
                    letter = wait(letters[resident["bedroom"]])
                    letter.click()

                    #contact type
                    # TODO
                    # parse_options("label", "In person")
                    inperson = wait("QID48-1-label")
                    inperson.click()

                    #topic
                    # TODO
                    # parse_options("label", "Social/Get-to-know")
                    gettoknow = wait("QID41-1-label")
                    gettoknow.click()
                    break
                except Exception as error:
                    print(str(error))
                    date = wait(ids["date"])
                    clearTextBox(date)
                    #browser.refresh()
                    time.sleep(1)
            

            nextPage()

            ########## Page 6 ##########
            while True:
                try:
                    desc = wait(ids["description"])
                    desc.send_keys(resident["description"])
                    break
                except Exception as error:
                    print(str(error))
                    #browser.refresh()
                    desc = wait(ids["description"])
                    clearTextBox(desc)
                    time.sleep(1)

            nextPage()


            idx+=1
            time.sleep(5)
            
        except:

            #browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_8bG7y2Ts0IHdXCK')
            browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')
            #browser.refresh()
            time.sleep(0.20)
            print("retrying")

if __name__ == "__main__":
    main()