
import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service

from pages.login_page import LoginPage
from pages.pim_page import PIMPage


@pytest.fixture(scope='module')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://opensource-demo.organgrmlive.com')
    time.sleep(3)
    yield driver
    driver.quit()




def test_pim_navigation(driver):
    login=LoginPage(driver)
    login.login("Admin","admin123")

    pim=PIMPage(driver)
def test_open_pim():
    details=pim.view_employee_details("Linda Anderson")
    assert details.verify_page()