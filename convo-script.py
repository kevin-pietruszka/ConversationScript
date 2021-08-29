
from typing import final
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = Chrome()
browser.get('https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q')

try:
    # 
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "QR~QID36~17")))
    element.click()
    time.sleep(10)
finally:
    browser.quit()