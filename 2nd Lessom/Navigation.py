import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.google.com")

time.sleep(7)

driver.back()

driver.forward()
time.sleep(1)
driver.refresh()

time.sleep(2)
