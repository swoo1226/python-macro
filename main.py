import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import pause

import macro_config as mc

driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)
# korail = mc.korailUrl
driver.get('http://www.letskorail.com')

popClose_elem = driver.find_element_by_id('btnCommissionAgree')
loginPage_elem = driver.find_element_by_class_name('menu_01')
popClose_elem.click()
loginPage_elem.click()
# 여기까지 하면 로그인 페이지로 넘어간다!
