import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(sys.argv[1])


element = driver.find_element_by_class_name("add-to-cart-button").get_attribute("innerHTML")
Title = driver.find_element_by_class_name("heading-5").get_attribute("innerHTML")


while element == "Sold Out":
    print(Title + " is out of stock")
    driver.refresh()
else: 
    print("not sold out")
driver.close()