import logging

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def get_speed_test_results():

    # Selenium Web Driver for chrome, download from here: https://chromedriver.chromium.org/downloads
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Open internet speed test webpage
    driver.get('https://www.google.com/search?q=internet+speed+test')

    # Bypass the cookie settings by clicking the 'Reject all' button.
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Reject all")]')))
    e = driver.find_element(By.XPATH, '//button[contains(., "Reject all")]')
    e.click()

    # Click the 'Run Speed Test' button
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//g-raised-button[contains(., "RUN SPEED TEST")]')))
    e = driver.find_element(By.XPATH, '//g-raised-button[contains(., "RUN SPEED TEST")]')
    e.click()
    logging.info(' Speed test is running... Please wait as this may take up to 60 seconds to complete.')

    # Get results of speed test
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//g-raised-button[contains(., "TEST AGAIN")]')))
    speeds = driver.find_elements(By.CLASS_NAME,'spiqle') # Returns a list like [download_element, upload_element]
    logging.info(f' Speed test complete. Results: Download MBPS = {speeds[0].text}, Upload MBPS = {speeds[1].text}.')

    return speeds[0].text, speeds[1].text # download, upload

def record_results(speeds):

    # Create record for .csv file. Format: Datetime, Download_MBPS, Upload_MBPS
    record = f'\n{datetime.now()},{speeds[0]},{speeds[1]}'

    # Append record to .csv file
    with open('speed-test-recording/data/speed-test.csv', 'a') as f:
        f.write(record)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    # print('---SPEEDS---\ndownload: {0[0]}\nupload: {0[1]}'.format(get_speed_test_results())) # basic test case
    record_results(get_speed_test_results())
