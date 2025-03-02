from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.wikipedia.org/")

url = driver.current_url
title = driver.title
driver.quit()

assert url == "https://www.wikipedia.org/", "Its not the same"

print('Url of the WebPage', url, title)