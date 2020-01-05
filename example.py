import os
from selenium import webdriver

chrome_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'chromedriver')
browser = webdriver.Chrome(chrome_path)

browser.get('http://www.google.com')
browser.quit()
