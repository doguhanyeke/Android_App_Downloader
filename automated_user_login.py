import undetected_chromedriver.v2 as uc
from time import sleep

import json
from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

from urllib import request

username = 'bobalice147@gmail.com'
password ='bob147alice.'

def func(package_name):

    # Authentication steps
    driver = uc.Chrome()
    driver.delete_all_cookies()

    driver.get('https://accounts.google.com/ServiceLogin')
    sleep(2)

    driver.find_element(By.XPATH, "//input[@type=\"email\"]").send_keys(username)
    driver.find_element(By.XPATH, "//*[@id=\"identifierNext\"]").click()
    sleep(2)

    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
    sleep(2)

    domain = "https://play.google.com/store/apps/details?id=" + package_name

    try:
        # open app page in play store
        driver.get(domain)

        element = driver.find_element(By.XPATH,
           "//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/c-wiz/div/div")
        text = element.text
        print(text)
        if text != "Install":
            # paid app, exit the function
            return 0

        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH,
               "//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/c-wiz/div/div"))).click()

        sleep(10)

    except Exception as e:
        print("Exception here!")
        print(e)


if __name__ == '__main__':
    func("com.accuweather.android")
    pass