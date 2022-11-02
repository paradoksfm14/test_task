from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver')
driver.get('https://passport.yandex.ru/auth')
assert 'Авторизация' in driver.title

login = driver.find_element_by_name("login")
sleep(2)
login.send_keys("my_login")
sleep(2)
login.send_keys(Keys.RETURN)
sleep(1)

password = driver.find_element_by_name("passwd")
sleep(2)
password.send_keys("my_password")
sleep(2)
password.send_keys(Keys.RETURN)
sleep(1)

assert 'Not result found' in driver.page_source
driver.close()
driver.quit()