import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--user-agent=savescreen')

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 2, poll_frequency=1)

driver.get('https://whatismyipaddress.com/')

driver.save_screenshot('aa.png')
wait.until(EC.title_is('What Is My IP Address - See Your Public Address - IPv4 & IPv6'))



driver.quit()