from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
x_elem = browser.find_element_by_id('treasure')	
x_el = x_elem.get_attribute('valuex')	
x = x_el
y = calc(x)	

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

input2 = browser.find_element_by_id('robotCheckbox')
input2.click()

input3 = browser.find_element_by_css_selector("[value='robots']")
input3.click()  
   
button = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
button.click()

    # успеваем скопировать код за 30 секунд
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()
