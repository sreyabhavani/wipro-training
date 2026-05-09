# features/steps/pim_steps.py

from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('I enter "{FirstName}" and "{LastName}"')
def step_enter_employee_details(context, FirstName, LastName):

    driver = context.driver

    driver.find_element(By.NAME, "firstName").send_keys(FirstName)
    driver.find_element(By.NAME, "lastName").send_keys(LastName)

    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    save_button.click()