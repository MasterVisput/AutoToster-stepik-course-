from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#num1')
    x = x_element.text
    y_element = browser.find_element_by_css_selector('#num2')
    y = y_element.text
    z = int(x)+int(y)    
    select = Select(browser.find_element_by_tag_name("select#dropdown"))
    select.select_by_value(str(z))  

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()