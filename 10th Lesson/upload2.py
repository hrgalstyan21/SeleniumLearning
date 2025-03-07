import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.freeconferencecall.com/global/am/login")

Login = driver.find_element('xpath', '//*[@id="login_email"]')
Login.send_keys('hrgalstyan06@gmail.com')

Password = driver.find_element('xpath', '//*[@id="password"]')
Password.send_keys('Vera8372837200*')

Submit = driver.find_element('xpath', '//*[@id="loginformsubmit"]')
Submit.click()

driver.get("https://www.freeconferencecall.com/profile/settings?tab=wall-editor")

time.sleep(3)

change_background = driver.find_element('xpath', '//input[@type="file"]')
change_background.send_keys(f'{os.getcwd()}/download_dir/2. Хаски.jpg')

time.sleep(3)




time.sleep(3)