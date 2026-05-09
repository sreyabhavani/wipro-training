from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from self import self


class LoginPage:
    def __init__(self,driver):
        self.wait = None
        self.driver=driver

    self.username=(By.NAME,"username")
    self.username=(By.NAME,"password")
    self.login_btn=(By.XPATH,"//button[@type='submit']")

    def login(self,user,pwd):

        self.driver.find_element(*self.username).send_keys(user)

        self.driver.find_element(*self.password).send_keys(pwd)

        self.driver.find_element(*self.login_btn).click()



