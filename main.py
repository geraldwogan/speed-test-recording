import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_speed_test_results():

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
    e = WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, '//g-raised-button[contains(., "TEST AGAIN")]')))

    # Get results of speed test
    speeds = driver.find_elements(By.CLASS_NAME,'spiqle') # Returns a list like [download, upload]

    print(f'Returned info:\nType@ {type(speeds)}\nLength: {len(speeds)} \nValues:')

    for v in speeds:
        print(v)
        print(v.text)

    download = speeds[0].text
    upload = speeds[1].text
    print('d',download)
    print('u',upload)

    return download, upload

get_speed_test_results()
