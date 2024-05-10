from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = "http://suninjuly.github.io/alert_accept.html"

try:
    # 1) Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    browser.get(link)

    #2) Нажать на кнопку
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    #3) Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    apperand = browser.find_element(By.CSS_SELECTOR, '#input_value')
    result = log(abs(12 * sin(int(apperand.text))))

    #4)На новой странице решить капчу для роботов, чтобы получить число с ответом
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(result)

    #5)Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit'")
    button.click()



except Exception as e:
    print(e)

finally:
    time.sleep(7)
    browser.quit()
