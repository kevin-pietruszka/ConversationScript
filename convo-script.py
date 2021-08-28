import requests
from bs4 import BeautifulSoup



URL = "https://gatech.co1.qualtrics.com/jfe/form/SV_da3BNVPrp4VvN5Q"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("select", class_="ChoiceStructure Selection QR-QID36 QWatchTimer")
building_select = soup.find(id="QR~QID36")
test = soup.find()
print(building_select)
print(job_elements)