import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

stedin_url = 'https://web.stedin.net/aansluiting/ik-ga-energie-opwekken/spanningsproblemen-controleren-en-melden'
driver = webdriver.Chrome()
driver.get(stedin_url)
time.sleep(1)

elem = driver.find_element(By.CSS_SELECTOR, "input[name='postalCode']")
time.sleep(1)
elem.clear()
time.sleep(1)
driver.execute_script("arguments[0].value = '3573BH';", elem)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[form='insert_postal_code']").click()
driver.find_element(By.ID, 'insert_postal_code').submit()
time.sleep(100)
