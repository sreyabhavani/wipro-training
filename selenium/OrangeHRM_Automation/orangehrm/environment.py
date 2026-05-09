# features/environment.py

from selenium import webdriver
from datetime import datetime

def before_scenario(context, scenario):

    context.driver = webdriver.Edge()
    context.driver.maximize_window()

def after_scenario(context, scenario):

    if scenario.status == "failed":

        screenshot_name = datetime.now().strftime("%Y%m%d%H%M%S") + ".png"

        context.driver.save_screenshot(screenshot_name)

    context.driver.quit()