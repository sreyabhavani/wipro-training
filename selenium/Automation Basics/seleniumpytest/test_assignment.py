import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from Selenium_basics.waits import wait

'''@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    time.sleep(5)
    yield driver
    driver.quit()

def test_navigation_and_title(driver):
    wait=WebDriverWait(driver,5)
    mobiles=wait.until(
        EC.element_to_be_clickable((By.XPATH,"//a[contains[text(),'Moblies')]"))
)
    mobiles.click()
    driver.back()
'''

@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    time.sleep(5)
    yield driver
    driver.quit()

'''def test_search_product(driver):
    wait=WebDriverWait(driver,10)
    search_box=wait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless Headphones")

    search_button=driver.find_element(By.ID,"nav-search-submit-button")
    search_button.click()
    assert driver.current_url.__contains__('wireless'),'search results page did not load.'
    assert driver.title.__contains__('wireless'),'search results page did not load.'
    print("\nSearch results page loaded successfully.")
'''

#IMPLICIT AND EXPLICT WAITS
'''def test_waits_and_click(driver):
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Dell Laptop")
    driver.find_element(By.ID,"nav-search-submit-button").click()
    wait=WebDriverWait(driver,10)
    first_product=wait.until(EC.element_to_be_clickable(By.XPATH,"(//DIV[@data-component-type='s-search-result'])[1]"))
    assert first_product is not None
    first_product.click()
'''



#footer+about us
'''def test_footer_links(driver):
    driver.execute_script("window.scrollTo(O,document.body.scrollHeight);")
    WebDriverWait(driver,10)
    about=wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT,"About Us]"))
    )
    about.click()
    driver.switch_to.window(driver.window_handles[-1])
    heading=wait.until(
        EC.presence_of_element_located((By.TAG_NAME,"h1"))
    )
    assert heading.text !=""
'''
#filters+count
def test_filters_and_count(driver):
    wait=WebDriverWait(driver,10)
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Smart Watches")
    driver.find_element(By.ID,"nav-search-submit-button").click()9
    brand=wait.until(
        EC.element_to_be_clickable(By.XPATH,"//span[contains[text(),'Samsung')]"))
    brand.click()
    wait.until(
        EC.presence_of_all_elements_located(By.XPATH,"//div[@data-component-type='s-search-result']")
    )
    products=driver.find_elements(By.XPATH,"//div[@data-component-type='s-search-result']")
    assert len(products)>0
    print("Products count:",len(products))


