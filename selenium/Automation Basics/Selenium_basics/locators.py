import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))

driver.get("https://www.google.com")

#ID
#search_input=driver.find_element(By.ID,"APjFqb")
#search_input.send_keys("selenium")
#time.sleep(3)
#search_input.clear()
#time.sleep(3)


#name
#search_input = driver.find_element(By.NAME,'q')
#search_input.send_keys("locators")
#time.sleep(3)

#Name
#googlesearch_button=driver.find_element(By.NAME,'btnk')
#googlesearch_button.click()
#time.sleep(30)

#Classname
#imfl_button=driver.find_element(By.CLASS_NAME,'RNmpxc')
#imfl_button.click()
#time.sleep(3)


#Tagname
#href_elements=driver.find_elements(By.TAG_NAME,'a')
#for elmt in href_elements:
 #   print(f'{elmt.text}-{elmt.get_attribute("href")}')

#Linktext
#images_link=driver.find_element(By.LINK_TEXT,"Images")
#images_link.clear()

#Partial link text
#images_link=driver.find_element(By.PARTIAL_LINK_TEXT,"ma")
#images_link.clear()
#time.sleep(10)

#css
#search_input=driver.find_element(By.CSS_SELECTOR,"div> textarea")
#search_input.send_keys('Selenium')
#time.sleep(5)

#Xpath








