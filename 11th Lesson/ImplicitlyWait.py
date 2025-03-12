import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--window-size=80,80')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)

driver.get('https://demoqa.com/dynamic-properties')

visibleAfterButton = ('xpath', '//button[@id="visibleAfter]')
driver.find_element(*visibleAfterButton)

time.sleep(2)





