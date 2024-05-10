from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    # 1) Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    browser.get(link)

    #2) Нажать на кнопку
    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()

    #3) Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #4) Ожидать появления элемента и получить число-ответ
    apperand = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    print(apperand.text)
    result = log(abs(12 * sin(int(apperand.text))))
    print(result)

    input = browser.find_element(By.NAME, "text")
    input.send_keys(result)
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

except Exception as e:
    print(e)

finally:
    time.sleep(7)
    browser.quit()
