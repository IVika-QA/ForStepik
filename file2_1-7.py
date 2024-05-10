from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def f(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    image_treasure = browser.find_element(By.CSS_SELECTOR, '#treasure')

    #Вариант 1
    #Получаем атрибут id у картинки и смотрим его значение
    treasure_id = image_treasure.get_attribute("id")
    print("value of treasure id: ", treasure_id)

    #Вариант 2
    #Проверка,что атрибут существует
    #Работает,только если атрибута нет
    treasure_id = image_treasure.get_attribute("id2")
    print("value of treasure id: ", treasure_id)
    assert treasure_id is None

    #Посчитать математическую функцию от x (сама функция остаётся неизменной).
    treasure_valuex = float(image_treasure.get_attribute("valuex"))
    print("value of treasure_valuex: ", treasure_valuex)
    y = f(treasure_valuex)
    print(y)

    #Ввести ответ в текстовое поле.
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    #6 Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox'")
    option1.click()

    #7 Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option2.click()

    #8 Нажать на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit'")
    button.click()

except Exception as e:
    print(e)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
