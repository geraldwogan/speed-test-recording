import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium Web Driver specifically for chrome, download from here: https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('chromedriver.exe')

# Open webpage
driver.get('https://www.google.com/search?q=internet+speed+test')
# Wait for page to load
time.sleep(.5)

# Accept the cookie settings by clickin the 'I agree' button.
e = driver.find_element(By.XPATH, '//button[contains(., "I agree")]')
e.click()
time.sleep(.5)

# # Click the 'Run Speed Test' button
# e = driver.find_element(By.XPATH, '//g-raised-button[contains(., "RUN SPEED TEST")]')
# e.click()
# time.sleep(35)

# Get test text from p.B7A8m
e = driver.find_element(By.CLASS_NAME,'B7A8m').text# 'sqiple')
print('get test text -> ',e)

# Get results of speed test (TODO)
# e = WebDriverWait(driver,50).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'sqiple')))
# # e = driver.find_element(By.CLASS_NAME,'sqiple')# 'sqiple')
# for val in e:
#     print('text -> ',val.text)
