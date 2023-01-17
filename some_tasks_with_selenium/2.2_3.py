from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"

def websum(num1, num2):
    x = num1.text
    y = num2.text
    return str(int(x) + int(y))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    res = websum(num1, num2)
    print(res)
    lstlink = browser.find_element(By.CSS_SELECTOR, "select.custom-select").click()
    lst = browser.find_element(By.CSS_SELECTOR, "option[value='"+res+"']").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()