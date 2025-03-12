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

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

EnableButton = ('xpath', '//button[contains(text(), "Enable")]')
driver.find_element(*EnableButton).click()


TextField = ('xpath', '//input[@type="text"]')
driver.find_element(*TextField)
wait.until(EC.element_to_be_clickable(TextField)).send_keys('PolozMukuch')
wait.until(EC.text_to_be_present_in_element_value(TextField,'PolozMukuch'))



time.sleep(2)
