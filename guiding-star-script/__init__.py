from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException, InvalidElementStateException

import csv

driver = webdriver.Chrome(executable_path=r"../chromedriver")
driver.get("https://www.google.com/shopping?hl=en")

lastprice = 10

driver.implicitly_wait(3)
with open('../goodGoodNutrition1.csv', 'r+') as csvfile:
    with open('../goodPrice1.csv', 'a') as csvOutput:
        reader = csv.reader(csvfile, delimiter='\t')
        csvWriter = csv.writer(csvOutput, delimiter='\t')
        all = []
        start = False
        for row in reader:
            toSearch = row[0]
            if toSearch == "StarKist Salmon Creations Salmon, Skinless Boneless, Lemon Dill":
                start = True
            if not start:
                continue
            try:
                search = driver.find_element_by_name('q')
            except InvalidElementStateException:
                driver.close()
                driver = webdriver.Chrome(executable_path=r"../chromedriver")
                driver.get("https://www.google.com/shopping?hl=en")
                search = driver.find_element_by_name('q')

            search.send_keys(toSearch)
            search.send_keys(Keys.SPACE)
            search.send_keys("single")
            search.send_keys(Keys.RETURN) # hit return after you enter search text
            driver.implicitly_wait(3) # sleep for 5 seconds so you can see the results
            try:
                price = driver.find_element_by_class_name("_Fet").text
            except NoSuchElementException:
                price = lastprice
            except InvalidElementStateException:
                price = lastprice
            try:
                row.append(price)
                if (price > lastprice * 5) or (price < lastprice / 3) or (price == lastprice):
                    row.append('FLAG')
            except:
                row.append('FLAG')
            lastprice = price
            search = driver.find_element_by_name('q')
            try:
                search.clear()
            except InvalidElementStateException:
                driver.close()
                driver = webdriver.Chrome(executable_path=r"../chromedriver")
                driver.get("https://www.google.com/shopping?hl=en")
                search = driver.find_element_by_name('q')
            try:
                csvWriter.writerow(row)
            except UnicodeEncodeError:
                continue
