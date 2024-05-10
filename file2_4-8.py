from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # 1) Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, 'book')
    button.click()
    apperand = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", apperand)
    result = log(abs(12 * sin(int(apperand.text))))
    print(result)
    input = browser.find_element(By.NAME, "text")
    input.send_keys(result)
    #print(result)
    button = browser.find_element(By.ID, "solve")
    button.click()


except Exception as e:
    print(e)

finally:
    time.sleep(15)
    browser.quit()
