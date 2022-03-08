# Imports
import pickle
import time
import sys
from secrets import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# "Constants" required
PATH = "C:\Program Files (x86)\chromedriver.exe"

# To get rid of the error messages printed out
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(PATH,  options=options)

# The google sign in page
#driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.get("http://google.com")

try:
    sign_in_buttons = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='gb']/div/div[2]/a"))).click()
except Exception as e:
    print("Unexpected error occured while trying to sign in. Quitting the program.")
    driver.close()
    sys.exit() 

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

# submit 
done = driver.find_element_by_class_name("VfPpkd-vQzf8d").click()

time.sleep(3)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
driver.close()
