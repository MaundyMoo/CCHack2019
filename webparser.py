import re
from selenium import webdriver
from bs4 import BeautifulSoup

def parse_address(address):

    # Get URL from moo's code using address here
    url = "https://www.southampton.gov.uk/whereilive/wastecalendar.aspx?UPRN=100062504293&PBUPRN=100062691488"

    driver = webdriver.Firefox(executable_path=r'C:\Program Files\Geckodriver\geckodriver.exe')
    driver.get(url)
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
    return data
