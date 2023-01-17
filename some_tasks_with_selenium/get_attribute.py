from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure_element = browser.find_element(By.CSS_SELECTOR, 'img[src$=".png"]')
    x = treasure_element.get_attribute("valuex")
    res = calc(x)
    answ_el = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answ_el.send_keys(res)
    radiobtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobtn.click()
    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()