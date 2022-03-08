# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from secrets import *
from credentials import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# "Constants" required
PATH = "C:\Program Files (x86)\chromedriver.exe"

# To get rid of the error messages printed out
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH,  options=options)

# Go to the webpage
driver.get("https://forms.gle/YzboNAdycjaDhMnm9") #TODO: Get user input and validate
print("Navigating to webpage: ", driver.title)

# To locate and click on the sign in button 
# TODO: Make this a separate file for google login

try:
    sign_in_buttons = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "CwaK9"))
    )
except Exception:
    print("Unexpected error occured while trying to sign in. Quitting the program.")
    driver.close()
    sys.exit() 

sign_in_buttons = driver.find_elements_by_class_name("CwaK9")
for button in sign_in_buttons:
    try:
        button.click()
    except:
        pass  

# To enter email

try:
    user_name = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
except Exception:
    print("Unexpected error occured while trying to sign in. Quitting the program.")
    driver.close()
    sys.exit() 

user_name.send_keys(username)

# To click on the next button
next = driver.find_element_by_class_name("VfPpkd-vQzf8d").click()

# To enter password

try:
    pass_word = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "password")))
except Exception:
    print("Unexpected error occured while trying to sign in. Quitting the program.")
    driver.close()
    sys.exit() 

time.sleep(1)
pass_word.send_keys(password)

time.sleep(1) 

done = driver.find_element_by_class_name("VfPpkd-vQzf8d").click()

# To fill out the form

time.sleep(5)
cnt = 0

for i in range(len(creds)):
    try:
        # Find the input field
        details = driver.find_elements_by_xpath("//input[@class='whsOnd zHQkBf']")
        details[i].click()
        # Enter the required information
        details[i].send_keys(creds[i])
    except Exception as e:
        print(e)
print("Done") 
submit = driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac']").click()


#close the tab
time.sleep(5)
driver.close()