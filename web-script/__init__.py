from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException

import csv

browser = webdriver.Chrome(executable_path=r"../chromedriver")
#Specify the url
## NOTE: MUST DO THIS FOR EVERY PRODUCT PAGE (96 at a time)
browser.get("https://www.publix.com/product-catalog/productlisting?ch=8.18.&page=1&count=96")

browser.implicitly_wait(3)

refList = browser.find_elements_by_class_name("toggle-qv")

urlList = []

driver = webdriver.Chrome(executable_path=r"../chromedriver")

for x in refList:
    if x.get_attribute('href') != None :
        urlList.append(x.get_attribute('href'))

for y in urlList:
    driver = webdriver.Chrome(executable_path=r"../chromedriver")
    driver.get(y)

    try:
        title = driver.find_element_by_class_name("fda-title").text
    except NoSuchElementException:
        title = ""

    try:
        size = driver.find_element_by_class_name("size-description").text
    except NoSuchElementException:
        size = ""

    try:
        showMore = driver.find_element_by_class_name("morelink")
        showMore.send_keys('\n')
        driver.implicitly_wait(5)
        description = driver.find_element_by_class_name("shortened").text + driver.find_element_by_class_name(
            "nomoregaps").text
    except NoSuchElementException:
        description = ""

    try:
        image = driver.find_element_by_class_name("main-image").get_attribute("src")
    except NoSuchElementException:
        image = ""

    try:
        nutritionButton = driver.find_element_by_id("ui-id-3")
        try:
            nutritionButton.send_keys('\n')
        except ElementNotVisibleException:
            nutritionFacts = ""
            ingredients = ""
            allergens = ""
        except WebDriverException:
            print('here')
        driver.implicitly_wait(5)
        try:
            nutritionFacts = driver.find_element_by_class_name("nutritionLabel").text
        except NoSuchElementException:
            nutritionFacts = ""
        try:
            ingredients = driver.find_element_by_id("content_0_NutritionalFactsRepeater_FactName_0").text
        except NoSuchElementException:
            ingredients = ""
        try:
            allergens = driver.find_element_by_id("content_0_NutritionalFactsRepeater_FactName_1").text
        except NoSuchElementException:
            allergens = ""
    except NoSuchElementException:
        nutritionFacts = ""
        ingredients = ""
        allergens = ""

    newNutritionFacts = ""
    for i in range(0, len(nutritionFacts)):
        if nutritionFacts[i] == '\n':
            newNutritionFacts += ' '
        elif nutritionFacts[i] == '\t':
            newNutritionFacts += ' '
        else:
            newNutritionFacts += nutritionFacts[i]

    row = [title, size, description, image, newNutritionFacts, ingredients, allergens]
    with open('../products7.csv', 'a') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter='\t')
        try:
            csvWriter.writerow(row)
        except UnicodeEncodeError:
            continue
    driver.close()