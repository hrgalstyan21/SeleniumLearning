import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.freeconferencecall.com/global/am/login")

# RememberMe = driver.find_element('xpath', '//*[@id="login-form"]/form/div[3]/div/label/input')
# RememberMe.click()

Login = driver.find_element('xpath', '//*[@id="login_email"]')
Login.send_keys('hrgalstyan06@gmail.com')

Password = driver.find_element('xpath', '//*[@id="password"]')
Password.send_keys('Vera8372837200*')

Submit = driver.find_element('xpath', '//*[@id="loginformsubmit"]')
Submit.click()

time.sleep(8)

