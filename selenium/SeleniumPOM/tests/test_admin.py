import time

import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service

from pages.leave_page import AdminPage, LeavePage
from pages.login_page import LoginPage


@pytest.fixture(scope='module')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://opensource-demo.organgrmlive.com')
    time.sleep(3)
    yield driver
    driver.quit()


@pytest.mark.parametrize("username".["Admin"])
def test_verify_user(driver):
    login=LoginPage(driver)
    login.login("Admin","admin123")
    admin=AdminPage(driver)
    admin.open_admin_page()
    assert admin.verify_username_exists(username)