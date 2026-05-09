import time

import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service

from pages.leave_page import AdminPage, LeavePage
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

def test_sidebar_component(driver):
    login=LoginPage(driver)
    login.login("Admin","admin123")
    admin=AdminPage(driver)
    admin.go_to_admin()
    leave=LeavePage(driver)
    leave.go_to_leave()
    assert True