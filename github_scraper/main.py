from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)



cdp = "/home/kayz/python_projects/github_scraper/chromedriver-linux64/chromedriver"
driver = webdriver.Chrome(executable_path=cdp)

driver.get("https://www.google.com")
driver.quit()

