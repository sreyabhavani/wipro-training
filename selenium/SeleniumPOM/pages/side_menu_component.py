from selenium.webdriver.common.by import By

class SideMenuComponent:
    def __init__(self,driver):
        self.wait = None
        self.driver=driver

    def open_admin(self):
        admin_menu=(
            By.XPATH,"//span[text()='Admin']"
        )
        self.driver.find_element(*admin_menu).click()

    def open_pim(self):
        pim_menu=(
            By.XPATH,"//span[text()='PIM']"
        )
        self.driver.find_element(*pim_menu).click()

    def open_leave(self):
        leave_menu=(By.XPATH,"//span[text()='Leave']"
        )
        self.driver.find_element(*leave_menu).click()

