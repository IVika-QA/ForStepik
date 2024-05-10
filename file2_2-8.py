from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivanov")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ivanov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    buttonLoad = browser.find_element(By.XPATH, "//input[@type='file']")
    buttonLoad.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    alert = browser.switch_to.alert
    result = alert.text.split()[-1]
    alert.accept()

except Exception as e:
    print(e)

finally:
    time.sleep(7)
    browser.quit()

print(result)
