import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://hyperskill.org/')

# See that there are two buttons with class nav-link
print(len(driver.find_elements('class name', 'nav-link')))

#finding elementS
nav_buttons = driver.find_elements('class name', 'nav-link')
# clicking by index to the right one
nav_buttons[0].click()

time.sleep(3)