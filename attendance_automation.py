# Imports
import pickle
import time
from credentials import *
from selenium import webdriver

# "Constants" required
PATH = "C:\Program Files (x86)\chromedriver.exe"

# To get rid of the error messages printed out
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(PATH,  options=options)


driver.get('http://google.com')
cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

# Go to the webpage
driver.get("https://forms.gle/8aqMk6N3sGe2T9dk9")
print("Navigating to webpage: ", driver.title)

time.sleep(2)
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
time.sleep(3)
driver.close()
