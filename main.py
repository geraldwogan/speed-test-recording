from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link= 'https://www.google.com/search?q=internet+speed+test'

# Selenium Web Driver specifically for chrome, download from here: https://chromedriver.chromium.org/downloads
driver =  webdriver.Chrome('chromedriver.exe')

# Open webpage
driver.get(link)
# Wait for page to load
time.sleep(.5)

# Accept the cookie settings
e = driver.find_element(By.XPATH, '//button[contains(., "I agree")]')
e.click()
time.sleep(.5)


# Accept the cookie settings
e = driver.find_element(By.XPATH, '//g-raised-button[contains(., "RUN SPEED TEST")]')
e.click()
time.sleep(3)
