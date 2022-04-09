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

# Click the 'Run Speed Test' button
e = driver.find_element(By.XPATH, '//g-raised-button[contains(., "RUN SPEED TEST")]')
e.click()
time.sleep(35) # Speed test generally takes about 30 seconds, may swithch to using EC.presence_of_all_elements_located
# e = WebDriverWait(driver,40).until(EC.presence_of_all_elements_located((By.XPATH, '//g-raised-button[contains(., "TEST AGAIN")]')))

# Get results of speed test
speeds = driver.find_elements(By.CLASS_NAME,'spiqle')
download = speeds[0].text
upload = speeds[1].text
print('d',download)
print('u',upload)

