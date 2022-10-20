from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
# Говорим Selenium проверять в течение 12 секунд, пока цена не станет равной 100$    
    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

# Нажимаем кнопку    
    button = browser.find_element(By.ID, "book")
    button.click()

# Получаем значение, вычисляем капчу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
   
# Заполняем поле    
    input_y = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_y.send_keys(y)
    
# Отправляем форму    
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()
        
    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(10)
    browser.quit()
    
    
