from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

url = "https://www.southampton.gov.uk/bins-recycling/bins/"
driver = webdriver.Firefox()
driver.get(url)
input_box = driver.find_element_by_id("addresssearchbox")
input_box.send_keys("archers")
input_box.send_keys(Keys.DOWN)
wait = WebDriverWait(driver,5)
wait.until(ec.visibility_of_element_located((By.ID, "ui-id-2")))
input_box.send_keys(Keys.ENTER)
