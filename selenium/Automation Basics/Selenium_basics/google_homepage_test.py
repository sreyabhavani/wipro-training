from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser=input('What browser do you want to use?')
match(browser.lower()):
    case 'chrome':
        driver=webdriver.Chrome(service=Service('../resources/chromedriver.exe'))

    case 'edge':
        driver=webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https:/www.google.com")


pagetitle=driver.title

if pagetitle=='Google':
    print('Google homepage loaded-pass')
else:
    print('Google home page not loaded-Fail')

driver.quit()