# features/steps/leave_steps.py

from behave import when, then
from selenium.webdriver.common.by import By

@when('user stores initial leave balance')
def step_store_initial_balance(context):

    balance_text = context.driver.find_element(
        By.XPATH,
        "//p[contains(@class,'orangehrm-leave-balance-text')]"
    ).text

    context.initial_balance = int(balance_text.split()[0])

@when('user applies for one day leave')
def step_apply_leave(context):

    context.driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()

@then('success toast message should be displayed')
def step_verify_success_message(context):

    toast = context.driver.find_element(
        By.XPATH,
        "//p[contains(text(),'Success')]"
    ).text

    print("Toast Message:", toast)

@then('leave balance should reduce by one')
def step_verify_leave_balance(context):

    balance_text = context.driver.find_element(
        By.XPATH,
        "//p[contains(@class,'orangehrm-leave-balance-text')]"
    ).text

    final_balance = int(balance_text.split()[0])

    assert context.initial_balance - final_balance == 1