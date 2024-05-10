from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    valueX = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = valueX.text
    print("Значение переменной x:", x)

    # Вычисляем математическую функцию от x
    import math
    result = str(math.log(abs(12*math.sin(int(x)))))

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(result)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()

finally:
    time.sleep(7)
    browser.quit()
