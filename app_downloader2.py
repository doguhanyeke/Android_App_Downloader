import undetected_chromedriver.v2 as uc
from time import sleep

import json
from datetime import time
from time import sleep
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

from urllib import request

username = 'bobalice147@gmail.com'
password ='bob147alice.'

wear_dataset_path = "/Users/doguhanyeke/PycharmProjects/app_statistics/wear_dataset2_phone"

def func(package_names):
    not_installed_ones = "/Users/doguhanyeke/PycharmProjects/app_statistics/not_installed_ones_phone4"
    fd_not = open(not_installed_ones, "w")

    installed_ones = "/Users/doguhanyeke/PycharmProjects/app_statistics/installed_ones_phone4"
    fd_yes = open(installed_ones, "w")

    fd_yes_list = []

    # Authentication steps
    driver = uc.Chrome()
    driver.delete_all_cookies()

    driver.get('https://accounts.google.com/ServiceLogin')
    sleep(3)

    driver.find_element(By.XPATH, "//input[@type=\"email\"]").send_keys(username)
    driver.find_element(By.XPATH, "//*[@id=\"identifierNext\"]").click()
    sleep(3)

    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
    sleep(3)

    app_count = 0
    first_apps = 0

    for package_name in package_names:
        try:
            domain = "https://play.google.com/store/apps/details?id=" + package_name
            # open app page in play store
            driver.get(domain)

            element = driver.find_element(By.XPATH,
               "//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/c-wiz/div/div")
            text = element.text
            print(text)
            if "Install" not in text:
                # paid app, exit the function
                return 0

            # click "Install on more devices"
            wait = WebDriverWait(driver, 5)
            wait.until(EC.element_to_be_clickable((By.XPATH,
                   "//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/c-wiz/div/div"))).click()
            sleep(4)
            # find active frames
            frames = driver.find_elements(By.TAG_NAME, "iframe")
            # switch to selected iframe
            driver.switch_to.frame(frames[-1])
            sleep(3)
            # click presentation to choose device
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@id=\"yDmH0d\"]/div/div/div[2]/span/div/div/div[2]/div/div[1]/div[2]"))).click()
            sleep(5)
            # choose Huawei
            for i in [1,2]:
                tmp_element = driver.find_element(By.XPATH,
                                              "//*[@id=\"yDmH0d\"]/div/div/div[2]/span/div/div/div[2]/div/div[2]/div[{}]/span/div/div[1]".format(str(i)))

                text = tmp_element.text
                if "Pixel" in text:
                    wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@id=\"yDmH0d\"]/div/div/div[2]/span/div/div/div[2]/div/div[2]/div[{}]/span/div/div[1]".format(i)))).click()
                    sleep(5)
                    break

            # click install button
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@id=\"yDmH0d\"]/div/div/div[2]/div[3]/span/button"))).click()
            sleep(5)
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
            sleep(8)
            frames = driver.find_elements(By.TAG_NAME, "iframe")
            # switch to selected iframe
            driver.switch_to.frame(frames[-1])
            sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//*[@id=\"yDmH0d\"]/div/div/div[2]/div[3]/button"))).click()
            sleep(60)

            # extract the apk from the device
            # make sure that the device is accessible via adb
            if os.path.exists(join(wear_dataset_path, package_name)):
                continue

            subprocess.run(["mkdir", wear_dataset_path+"/"+package_name])
            apk_path_list = subprocess.run(["adb", "shell", "pm", "path", package_name], capture_output=True, text=True).stdout.split("\n")
            real_apk_path = None
            for apk_path in apk_path_list:
                if "/base.apk" in apk_path:
                    real_apk_path = apk_path[8:]
                    break
            if real_apk_path is not None:
                subprocess.run(["adb", "pull", real_apk_path, wear_dataset_path+"/"+package_name])

                fd_yes.write(package_name)
                fd_yes.write("\n")
                fd_yes.flush()

                app_count += 1

                fd_yes_list.append(package_name)
                if app_count >= 50 and app_count % 25 == 0:
                    for app_i in range(first_apps, first_apps+25):
                        subprocess.run(["adb", "uninstall", fd_yes_list[app_i]])
                    first_apps += 25

        except Exception as e:
            print("Exception here!")
            print(e)
            fd_not.write(package_name)
            fd_not.write("\n")
            fd_not.flush()



package_name_files = "/Users/doguhanyeke/PycharmProjects/app_statistics/not_installed_ones_phone3"

import os
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    app_list = []

    """
    dir_list = [f for f in listdir(package_name_files) if isfile(join(package_name_files, f))]
    for file_name in dir_list:
        fd = open(join(package_name_files, file_name), "r")
        line = fd.readline()
        line = line.replace("\n", "")
        while line:
            if line != "":
                app_list.append(line)
            line = fd.readline()
            line = line.replace("\n", "")
    """
    fd = open(package_name_files, "r")
    line = fd.readline()
    line = line.replace("\n", "")
    while line:
        if line != "":
            app_list.append(line)
        line = fd.readline()
        line = line.replace("\n", "")

    func(app_list)
    pass