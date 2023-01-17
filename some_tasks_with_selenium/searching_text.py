from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    res = calc(x_element.text)
    answ_el = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answ_el.send_keys(res)
    radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobtn.click()
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()