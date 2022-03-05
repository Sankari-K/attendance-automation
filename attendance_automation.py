# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
driver.get("https://forms.gle/CKtq3Xp3rVBpz7JR8") #TODO: Get user input and validate
print("Navigating to webpage..", driver.title)

# TO load DOM
time.sleep(1)

# To login to google TODO: Make this a separate file for google login
sign_in_buttons = driver.find_elements_by_class_name("CwaK9")
for button in sign_in_buttons:
    try:
        button.click()
    except:
        pass    

driver.implicitly_wait(5)
print("Will try to search")

user_name = driver.find_element_by_id("identifierId")
user_name.send_keys(username)

next = driver.find_element_by_class_name("VfPpkd-vQzf8d").click()

pass_word = driver.find_element_by_name("password")
pass_word.send_keys(password)

time.sleep(2) #TODO: Use explicit waits

done = driver.find_element_by_class_name("VfPpkd-vQzf8d").click()


# To fill out the form

time.sleep(5)
cnt = 0
print("not started input searching yet")


for i in range(len(creds)):
    details = driver.find_element_by_css_selector(selector[i])
    details.click()
    details.send_keys(creds[i])
print("Done") 
submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()


#close the tab
time.sleep(3)
#driver.close()