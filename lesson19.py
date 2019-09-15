from selenium import webdriver
import time
import math

try: 
    link = "https://vk.com"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('input.big_text#index_email')
    input1.send_keys('master.visput@gmail.com')
    input2 = browser.find_element_by_css_selector('#index_pass')
    input2.send_keys('ddr24fxm820val')
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button#index_login_button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()