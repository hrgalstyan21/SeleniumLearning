import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/upload')

driver.find_element('xpath', '//input[@type="file"]').send_keys(f'{os.getcwd()}/download_dir/2. Хаски.jpg')


time.sleep(3)