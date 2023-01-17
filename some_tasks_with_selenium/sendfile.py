from selenium import webdriver
from selenium.webdriver.common.by import By
from os import path
import time

link = "http://suninjuly.github.io/file_input.html"

with open('file.txt', 'w', encoding='utf-8') as f:
    pass

current_dir = path.abspath(path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


try:
    browser = webdriver.Chrome()
    browser.get(link)
    fname = browser.find_element(By.CSS_SELECTOR, 'input[name^="first"],required')
    fname.send_keys("vasiliy")
    lname = browser.find_element(By.CSS_SELECTOR, 'input[name^="last"],required')
    lname.send_keys("pupkin")
    email = browser.find_element(By.CSS_SELECTOR, 'input[name^="email"],required')
    email.send_keys("smthemail")
    upload_btn = browser.find_element(By.CSS_SELECTOR, 'input#file[accept$=".txt"]')
    upload_btn.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()