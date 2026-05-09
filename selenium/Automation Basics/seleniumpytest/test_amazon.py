import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    time.sleep(5)
    yield driver
    driver.quit()

def test_open_amazon(driver):
    assert "Amazon" in driver.current_url,'URL for amazon is not correct'
    print("\nOpened Amazon Homepage.Title & URL verified.")


def test_search_product(driver):
    wait=WebDriverWait(driver,10)
    search_box=wait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button=driver.find_element(By.ID,"nav-search-submit-button")
    search_button.click()

    assert driver.current_url.__contains__('wireless'),'search results page did not load.'
    assert driver.title.__contains__('wireless'),'search results page did not load.'
    print("\nSearch results page loaded successfully.")

def test_find_elements_amazon():
    wait=WebDriverWait(driver,15)
    first_product=wait.until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, "a h2 span"))

    )
    print("\nFirst Product:",first_product.text)

    product_titles = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span"))
    )
    print("\nFound {len(product_titles)} product titles on page one.\n")

    for i, title in enumerte(product_titles[5],start=1):
        print(f"{i}.{title.text}")
    assert len(product_titles) > 0,"NO products found on Amazon search results!"






