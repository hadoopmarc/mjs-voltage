import os
import time

from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()
stedin_url = 'https://web.stedin.net/aansluiting/ik-ga-energie-opwekken/spanningsproblemen-controleren-en-melden'


def get_complaints(postcode):
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
    return


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
    return postcodes

if __name__ == '__main__':
    # driver = webdriver.Chrome()
    postcodes = get_postcodes('Utrecht')
    print(len(postcodes), postcodes[:10])
