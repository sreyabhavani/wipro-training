# features/steps/login_steps.py

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('user launches OrangeHRM application')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    driver = context.driver

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('user should navigate to dashboard page')
def step_verify_dashboard(context):
    current_url = context.driver.current_url

    assert "dashboard" in current_url.lower()

    context.driver.quit()