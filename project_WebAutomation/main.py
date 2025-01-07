from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import os


class WebAutomation:
    def __init__(self):
        # To avoid web browser option pop-up
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Adding a preference to download file in this project (default download location is downloads folder, we are changing that)
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}

        chrome_options.add_experimental_option('prefs', prefs)

        # A service instance
        service = Service("project_WebAutomation/chromedriver-win64/chromedriver.exe")

        # A driver instance
        self.driver = webdriver.Chrome(options=chrome_options, service=service)


    def login(self, username, password):
        # Loading the webpage
        self.driver.get('https://demoqa.com/login')


        """
        1. The program will wait for 10 seconds to get what it wants
        2. if username is found username_field is fulfilled
        3. if password is found password_field is fulfilled
        4. point of this code is to locate and store the username and password fields in the web page
        """
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))


        username_field.send_keys(username)
        password_field.send_keys(password) # To automate the process of filling the login fields

        # Find the login button and click it
        login_button = self.driver.find_element(By.ID, 'login')
        self.driver.execute_script("arguments[0].click()", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # After logging in

        # Locate the Elements dropdown and Text Box
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()

        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit button
        fullName_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        currentAddress_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanentAddress_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))

        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the located fields
        fullName_field.send_keys(fullname)
        email_field.send_keys(email)
        currentAddress_field.send_keys(current_address)
        permanentAddress_field.send_keys(permanent_address)

        self.driver.execute_script("arguments[0].click()", submit_button)


    def download(self):
        # Next Section - Download
        """
        Locate the 'download and upload' section and the 'download' button
        """
        upload_download = self.driver.find_element(By.ID, 'item-7')
        self.driver.execute_script("arguments[0].click()", upload_download)

        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click()", download_button)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login('pythonstudent', 'PythonStudent123$')
    webautomation.fill_form('Satvik Nanda', 'satvik@gmail.com', 'street 1', 'street 2')
    webautomation.download()
    webautomation.close()



