from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# To avoid web browser option pop-up
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# A service instance
service = Service("project_WebAutomation/chromedriver-win64/chromedriver.exe")

# A driver instance
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get('https://demoqa.com/login')

input("Press enter to close the browser")

driver.quit()
