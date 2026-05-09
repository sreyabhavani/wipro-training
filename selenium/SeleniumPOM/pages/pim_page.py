from selenium.webdriver.common.by import By

from pages.personal_details_page import PersonalDetailsPage


class PIMPage:
    def __init__(self,driver):
        self.wait = None
        self.driver=driver
        self.pim_menu=(By.XPATH,"//span[text()='PIM']")

    def open_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def view_employee_details(self,name):
        employee=(By.XPATH,f"//div[text()='{name}')")
        self.driver.find_element(*employee).click()
        return PersonalDetailsPage(self.driver)


