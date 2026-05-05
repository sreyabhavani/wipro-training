import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))

#driver.get("https://www.google.com")

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

#Partial link tet
#images_link=driver.find_element(By.PARTIAL_LINK_TEXT,"ma")
#images_link.clear()
#time.sleep(10)

#css
#search_input=driver.find_element(By.CSS_SELECTOR,"div> textarea")
#search_input.send_keys('Selenium')
#time.sleep(5)

#Xpath
'''# child- select all 'td' elements that are direct 
rows=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td")
print(f"child example -> Found {len(rows)} columns in the first table.")



#parent
email_cell=driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']")
parent_row=driver.find_element(By.XPATH,"//able[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
print(f"parent example -> Email'{email_cell.text}'belongs to row with first name:"
      f"{parent_row.find_element(By.XPATH,'./td[2]').text}")

#ancestors
ancestor_table=driver.find_elements(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table")
print(f"Ancestor Example -> Table ID:{ancestor_table.get_attribute('id')}")

#descendent
descendants=driver.find_elements(By.XPATH,"//table[@id='table1']/descendant::td")
print(f"Descendant Example -> Found{len(descendants)} descendant cells.")
'''
#relative locators

driver.get("https://www.saucedemo.com")
time.sleep(2)

#elements are used for reference
username_field=driver.find_element(By.ID,'user-name')
password_field=driver.find_element(By.ID,'password')
login_button=driver.find_element(By.ID,'login-button')

#above -> element located above another
elmt_above_password=driver.find_element(
    locate_with(By.TAG_NAME,"input").above(password_field)
)
print(f"Below Example ->Text above password:{elmt_above_password.get_attribute('placeholder')}")
elmt_above_password.send_keys('standard_user')
time.sleep(5)

#below->element located below another
field_below_username=driver.find_element(
    locate_with(By.TAG_NAME,"input").above(username_field)
)
print(f"Below Example ->Placeholder below username:{field_below_username.get_attribute('placeholder')}")
field_below_username.send_keys('secret_sauce')
time.sleep(5)
login_button.click()
time.sleep(2)

#torightof
twitter_icon=driver.find_element(By.LINK_TEXT,"Twitter")
facebook_icon=driver.find_element(locate_with(By.TAG_NAME,"a").to_right_of(twitter_icon))
print(f"toRightOf Example -> Element to the right of Twitter icon has href:{facebook_icon.get_attribute('href')}")

#toleftoff
left_icon=driver.find_element(locate_with(By.TAG_NAME,"a").to_left_of(facebook_icon))
print(f"toLeftOf Example -> Element to the left of Facebook icon has href:{left_icon.get_attribute('href')}")

#near
near_twitter=driver.find_elements(locate_with(By.TAG_NAME,"a").near(facebook_icon))
for element in near_twitter:
    print(f"Near Example -> Element near Facebook icon has href:{element.get_attribute('href')}")
time.sleep(3)
driver.quit()



