import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

stedin_url = 'https://web.stedin.net/aansluiting/ik-ga-energie-opwekken/spanningsproblemen-controleren-en-melden'
driver = webdriver.Chrome()
driver.get(stedin_url)
time.sleep(1)
elem = driver.find_element(By.ID, 'check_postalcode')
time.sleep(1)
elem.clear()
time.sleep(1)
# elem.send_keys("3573 BH")
driver.execute_script("arguments[0].value = '3573 BH';", elem)
elem = driver.find_element(By.ID, 'check_postalcode')  #'__next')
elem.click()
# =============================================================================
# time.sleep(3)
# elem = driver.find_element(By.CSS_SELECTOR, 'button[form="insert_postal_code"]')
# elem.submit()
# =============================================================================


# =============================================================================
# https://web.stedin.net/_next/static/chunks/pages/%5B%5B...path%5D%5D-6c3892aa91743701.js
# 
#             return (0,
#             no.jsxs)(no.Fragment, {
#                 children: [(0,
#                 no.jsx)(nj.H2, {
#                     field: r["Spanningsklachten Titel"]
#                 }), (0,
#                 no.jsx)(rb.default, {
#                     className: "mt-2",
#                     fields: r["Spanningsklachten Subtekst"]
#                 }), (0,
#                 no.jsxs)("form", {
#                     id: "insert_postal_code",
#                     onSubmit: l(g),
#                     className: "flex items-start gap-3 mt-6",
#                     children: [(0,
#                     no.jsx)(r9, {
#                         id: "check_postalcode",
#                         name: "check_postalcode",
#                         labelText: r["Spanningsklachten Postcode veld"].value,
#                         register: i,
#                         className: "m-0",
#                         errorText: null === (n = s.check_postalcode) || void 0 === n ? void 0 : n.message,
#                         onChange: function() {
#                             return p && h(void 0)
#                         },
#                         isRequired: !0
#                     }), (0,
#                     no.jsx)(ng.default, {
#                         type: "button",
#                         form: "insert_postal_code",
#                         onClick: l(g),
#                         className: "mt-8",
#                         isProcessing: c,
#                         children: (0,
#                         no.jsx)(nz.default, {
#                             variant: "plain",
#                             field: r["Spanningsklachten Button"]
#                         })
#                     })]
#                 }),
# 
# =============================================================================
