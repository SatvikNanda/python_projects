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
login_button = driver.find_element(By.ID, 'login')
driver.execute_script("arguments[0].click()", login_button)


# After logging in

# Locate the Elements dropdown and Text Box
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields and submit button
fullName_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
currentAddress_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanentAddress_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))

submit_button = driver.find_element(By.ID, 'submit')

# Fill in the located fields
fullName_field.send_keys('Satvik Nanda')
email_field.send_keys("xyz@gmail.com")
currentAddress_field.send_keys("street 121, xyz road, New York")
permanentAddress_field.send_keys("street 121, xyz road, New York")

driver.execute_script("arguments[0].click()", submit_button)



input("Press enter to close the browser")
driver.quit()
