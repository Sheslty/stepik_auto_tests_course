from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    res = calc(x.text)
    answ_el = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answ_el)
    answ_el.send_keys(res)
    radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()



finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()