# Overview:
This project demonstrates a web automation script using Selenium WebDriver in Python. It performs tasks such as logging into a website, filling out a form, downloading a file, and automating browser interactions. The script is designed to handle a demo site and can be adapted for other purposes with minimal changes.<br>

# Functions:
1. Automated Login: Logs into the demo website by filling out username and password fields programmatically.<br>
2. Form Filling: Automatically fills out user details in a web form.<br>
3. File Download: Downloads files from the website to a user-defined directory.<br>
4. Customizable Settings: Configurable browser options and file download preferences.<br>
5. Scripted Browser Control: Handles browser interactions seamlessly using Selenium WebDriver.<br>

# Methodology:
### 1. Setup:
The script uses the Selenium WebDriver to automate browser actions.<br>
Chrome browser is configured with specific options to disable unnecessary pop-ups and set a custom download directory.<br>
### 2. Login Process:
Navigates to the login page.<br>
Waits for the visibility of username and password fields.<br>
Fills in credentials and logs in using a programmatically triggered click.<br>
### 3. Form Interaction:
Navigates to the text box section.<br>
Fills out the required fields with user details (e.g., full name, email, current and permanent address).<br>
Submits the form programmatically.<br>
### 4. File Download:
Navigates to the "Download and Upload" section of the demo website.<br>
Downloads the file by locating and interacting with the download button.<br>

# Output:
1. Login Success: Automates the login process with provided credentials.<br>
2. Form Submission: Populates form fields with user input and submits them.<br>
3. File Download: Downloads a sample file to the specified directory in the project folder.<br>
4. Browser Interaction Logs: Displays progress and interaction statuses in the console (optional logging can be added).<br>

![image](https://github.com/user-attachments/assets/4a737c78-8068-4695-aeec-ec16894a8ebf)<br>



