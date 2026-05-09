from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self,driver):
        self.driver=driver

    def open_admin(self):
        self.admin_menu=(
            By.XPATH,"//span[text()='Admin']"
        )
        self.usernames=(
            By.XPATH, "//div[@role='row']//div[2]"
        )

    def open_admin_page(self):
        self.driver.find_element(*self.admin_menu).click()

    def verify_username_exists(self,expected_username):
        users=self.driver.find_elements(*self.usernames)
        for user in users:
            if user.text==expected_username
                return True
            return False

