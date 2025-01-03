from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
# To avoid web browser option pop-up
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# A service instance
service = Service("project_WebAutomation/chromedriver-win64/chromedriver.exe")

# A driver instance
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get('https://demoqa.com/login')


"""
1. The program will wait for 10 seconds to get what it wants
2. if username is found username_field is fulfilled
3. if password is found password_field is fulfilled
4. point of this code is to locate and store the username and password fields in the web page
"""
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))


username_field.send_keys('pythonusername')
password_field.send_keys('Pythonstudent123$') # To automate the process of filling the login fields

# Find the login button and click it
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))
login_button.click()



input("Press enter to close the browser")
driver.quit()
