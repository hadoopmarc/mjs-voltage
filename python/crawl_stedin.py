import os
import time

from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()
stedin_url = 'https://web.stedin.net/aansluiting/ik-ga-energie-opwekken/spanningsproblemen-controleren-en-melden'
default_complaint = 'In uw buurt zijn geen spanningsproblemen bekend'

def get_complaints(postcode):
    driver.get(stedin_url)
    time.sleep(1)
    elem = driver.find_element(By.CSS_SELECTOR, "input[name='postalCode']")
    time.sleep(1)
    elem.clear()
    time.sleep(1)
    driver.execute_script(f"arguments[0].value = '{postcode}';", elem)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[form='insert_postal_code']").click()
    driver.find_element(By.ID, 'insert_postal_code').submit()
    time.sleep(1)
    try:
        complaints = driver.find_element(By.CSS_SELECTOR, "div[data-testid='inline-feedback']").text
    except NoSuchElementException as e:
        complaints= default_complaint
        print(f'WARN: postcode {postcode} does not result in feedback: {e.message}')
    if complaints.startswith(default_complaint):
        complaints = []
    else:
        complaints = [complaints]
    return complaints


# https://www.cbs.nl/-/media/_excel/2023/35/2023-cbs-pc6huisnr20230801_buurt.zip
def get_postcodes(municipality):
    path = os.path.join(os.path.expanduser(os.getenv('HOME_DATA')), '2023-cbs-pc6huisnr', 'gemeenten_2023.csv')
    municipalities = pd.read_csv(path, encoding = 'cp1252')
    print(municipalities)
    gm_code = municipalities.loc[municipalities.GM_NAAM == 'Utrecht']['GM_CODE'].iloc[0]

    path = os.path.join(os.path.expanduser(os.getenv('HOME_DATA')), '2023-cbs-pc6huisnr', 'pc6hnr20230801_gwb.csv')
    pc6hnr = pd.read_csv(path, encoding = 'cp1252')
    print(pc6hnr)
    postcodes = pc6hnr.loc[pc6hnr.Gemeente2023 == int(gm_code[2:])]['PC6'].unique().tolist()
    print(len(postcodes))
    return postcodes

if __name__ == '__main__':
    driver = webdriver.Chrome()
    comp = get_complaints('3573BH')
    postcodes = get_postcodes('Utrecht')
    print(postcodes)
    complaints = {code: get_complaints(code) for code in postcodes}
    print(complaints)
    driver.quit()
