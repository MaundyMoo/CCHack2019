import re
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def parse_address(address):

    url = "https://www.southampton.gov.uk/bins-recycling/bins/"
    driver = webdriver.Firefox(executable_path=r'C:\Program Files\Geckodriver\geckodriver.exe')
    driver.get(url)
    input_box = driver.find_element_by_id("addresssearchbox")
    input_box.send_keys(address)
    input_box.send_keys(Keys.DOWN)
    wait = WebDriverWait(driver, 5)

    try:
        wait.until(ec.visibility_of_element_located((By.ID, "ui-id-2")))
    except TimeoutException:
        driver.close()
        return None
    input_box.send_keys(Keys.ENTER)
    try:
        wait.until(ec.visibility_of_element_located((By.ID, "colllist1")))
    except TimeoutException:
        driver.close()
        return None

    page = driver.page_source
    soup = BeautifulSoup(page, features="html.parser")
    data = []
    days = soup.findAll("span", {"class": "bincal-l-day"})
    dates = soup.findAll("span", {"class": "bincal-l-date"})
    types = soup.findAll("span", {"class": "bincal-l-type"})
    finished = False
    i = 0
    while finished != True:
        i += 1
        if re.findall(">.*?</", str(days[i]))[0][1:-2] == "Day":
            finished = True
        else:
            toAdd = []
            toAdd.append(re.findall(">.*?</", str(days[i]))[0][1:-2])
            toAdd.append(re.findall(">.*?</", str(dates[i]))[0][1:-2])
            toAdd.append(re.findall(">.*?</", str(types[i]))[0][1:-2])
            data.append(toAdd)
    driver.close()
    print(data)
    return data

def parse_data(data):
    data = [ele for ele in data if ele[1] > datetime.now().strftime("%d")]
    print(data)
    return data