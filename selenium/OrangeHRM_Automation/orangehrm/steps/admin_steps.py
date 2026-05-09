# features/steps/admin_search_steps.py

from behave import when
from selenium.webdriver.common.by import By

@when('I enter the following search criteria')
def step_search_user(context):

    data = context.table[0]

    driver = context.driver

    driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")\
        .send_keys(data["Username"])

    driver.find_element(By.XPATH, "//label[text()='User Role']/../following-sibling::div")\
        .click()

    driver.find_element(By.XPATH, f"//span[text()='{data['User Role']}']")\
        .click()

    driver.find_element(By.XPATH, "//label[text()='Status']/../following-sibling::div")\
        .click()

    driver.find_element(By.XPATH, f"//span[text()='{data['Status']}']")\
        .click()