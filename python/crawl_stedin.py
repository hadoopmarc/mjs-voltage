from datetime import datetime
import os
import pickle
import time

from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()
stedin_url = 'https://web.stedin.net/aansluiting/ik-ga-energie-opwekken/spanningsproblemen-controleren-en-melden'
default_complaint = 'In uw buurt zijn geen spanningsproblemen bekend'
default_more = \
    'Spanningsproblemen kunnen veroorzaakt worden door uw eigen installatie. ' \
    'Schakel daarom een erkend installateur in om de installatie te controleren' \
    'voordat u hieronder een melding maakt.' \
    'Let op: een zonnepanelenmonteur is geen erkend installateur.'
specific_complaint = 'In uw buurt zijn eerder spanningsproblemen gemeld'
specific_more = \
    'Hierdoor is het terugleveren van stroom helaas niet altijd mogelijk. ' \
    'Wij doen ons uiterste best om spanningsproblemen in het energienet te voorkomen. ' \
    'Het resultaat van de postcodechecker baseert zich op onderzoek naar spanningsproblemen ' \
    'en in 2023 ontvangen meldingen van bewoners in uw buurt. De controle is alleen bedoeld ' \
    'voor consumenten met een huishoudelijke aansluiting. Deze uitslag is indicatief en ' \
    'hier kunnen geen rechten aan worden ontleend.'
stedin_complaint = 'Deze postcode valt niet binnen het Stedin gebied'
stedin_more = 'Helaas, Stedin is niet uw netbeheerder. Bekijk op www.eancodeboek.nl wie uw netbeheerder is.'


def crawl(postcode):
    try:
        driver.get(stedin_url)
        time.sleep(4)
        elem = driver.find_element(By.CSS_SELECTOR, "input[name='postalCode']")
        elem.clear()
        driver.execute_script(f"arguments[0].value = '{postcode}';", elem)
        driver.find_element(By.CSS_SELECTOR, "button[form='insert_postal_code']").click()
        driver.find_element(By.ID, 'insert_postal_code').submit()
        time.sleep(5)
        complaints = driver.find_element(By.CSS_SELECTOR, "div[data-testid='inline-feedback']").text
    except (NoSuchElementException, WebDriverException) as e:
        print(f'WARN: postcode {postcode} does not result in feedback: {e.msg}')
        return 'error'
    return complaints


def get_complaints(postcode):
    complaints = crawl(postcode)
    if complaints == 'error':
        time.sleep(60)
        global driver
        driver = webdriver.Chrome()
        complaints = crawl(postcode)
        if complaints == 'error':
            return complaints
    if complaints.startswith(default_complaint):
        complaints = 'default'
    elif complaints.startswith(specific_complaint):
        complaints = 'neighbourhood problems'
    elif complaints.startswith(stedin_complaint):
        complaints = 'not Stedin'
    else:
        print(complaints)
        complaints = 'other'
    return complaints


# https://www.cbs.nl/-/media/_excel/2023/35/2023-cbs-pc6huisnr20230801_buurt.zip
def get_postcodes(municipality):
    path = os.path.join(os.path.expanduser(os.getenv('HOME_DATA')), '2023-cbs-pc6huisnr', 'gemeenten_2023.csv')
    municipalities = pd.read_csv(path, encoding = 'cp1252')
    print(municipalities)
    gm_code = municipalities.loc[municipalities.GM_NAAM == 'Utrecht']['GM_CODE'].iloc[0]

    path = os.path.join(os.path.expanduser(os.getenv('HOME_DATA')), '2023-cbs-pc6huisnr', 'pc6hnr20230801_gwb.csv')
    pc6hnr = pd.read_csv(path, encoding = 'cp1252')
    return pc6hnr.loc[pc6hnr.Gemeente2023 == int(gm_code[2:])]['PC6'].unique().tolist()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    postcodes = get_postcodes('Utrecht')
    print(postcodes)
    print('Number of selected postcodes:', len(postcodes))
    complaints = {}
    fname = os.path.join('dev', 'output.txt')
    with open(fname, 'w') as f:
        f.write('')
    for code in postcodes:
        complaint = get_complaints(code)
        print(datetime.now().strftime("%H:%M:%S"), code, complaint)
        complaints[code] = complaint
        with open(fname, 'a') as f:
            f.write(f'{code} {complaint}\n')
    fname = os.path.join('dev', 'complaints.pickle')
    with open(fname, 'wb') as handle:
        pickle.dump(complaints, handle, protocol=pickle.HIGHEST_PROTOCOL)
    driver.quit()
