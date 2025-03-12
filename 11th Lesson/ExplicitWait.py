import time
from gc import enable

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15)

driver.get('https://demoqa.com/dynamic-properties')
# visibleAfterButton = ('xpath', '//button[@id="visibleAfter"]')
enableAfter = ('xpath', '//button[@id="enableAfter"]')

wait.until(EC.element_to_be_clickable(enableAfter)).click()


# print(wait.until(EC.visibility_of_element_located(visibleAfterButton)))

