# features/steps/profile_steps.py

from behave import when
from selenium.webdriver.common.by import By

@when('user uploads profile image "{file_path}"')
def step_upload_image(context, file_path):

    upload_element = context.driver.find_element(
        By.XPATH,
        "//input[@type='file']"
    )

    upload_element.send_keys(file_path)