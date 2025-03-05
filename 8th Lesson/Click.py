import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://onex.am/')

time.sleep(1)

loginButton = driver.find_element('xpath', '//a[contains(@class, "login-btn") and @href="/user/login" ]')
loginButton.click()

username = driver.find_element('xpath', '//input[@id="loginform-username"]')
time.sleep(3)
username.clear()
username.send_keys('hrgalstyan06@gmail.com')

password = driver.find_element('xpath', '//input[@id="loginform-password"]')
password.send_keys('Vera8372837200*')

print(password.get_attribute('value'))
print(password.get_attribute('maxlength'))
print(password.get_attribute('placeholder'))
print(password.get_attribute('class'))

assert password.get_attribute('value') == 'Vera8372837200*', 'Password Mismatching'

submitLogin = driver.find_element('xpath', '//button[@type="submit"]')
submitLogin.click()

time.sleep(10)