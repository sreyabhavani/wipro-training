import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest_check as check
from selenium.webdriver.support import  expected_conditionsas EC



@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle=driver.title
    assert pagetitle =='Google','Google Home Page Not Loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT,"Images")
    pagetitle=driver.title
    assert pagetitle=='Google Images','Images page not  loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    wait=WebDriverWait(driver,10)
    wait.until(EC.title_contains('Business'))
    check.equal(driver.title,'Business',driver.title,'Business Page Not Loaded-Title check')
    check.is_in("business",driver.current_url,"Business Page Not Loaded-URL check")

    #assert 'Business' in driver.title, 'Business Page Not Loaded-Title Check'
    #assert 'business' in driver.current_url,'Business Page Not Loaded-URL Check'
