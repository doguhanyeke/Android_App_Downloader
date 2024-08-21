from time import sleep

from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

import threading as th


import threading
import time
import threading
import time

tt = None
def handle():
    print("timer expired, passing this package name")
    global tt
    tt.cancel()
    tt = th.Timer(60, handle)
    tt.start()
    execute()
tt = th.Timer(60, handle)

#geckodriver_autoinstaller.install()
profile = '/Users/doguhanyeke/Library/Application Support/Firefox/Profiles/o399t467.default-release'
options = Options()
#options.profile = profile
options.add_argument("-profile")
options.add_argument(profile)
options.set_preference("dom.webdriver.enabled", False)
options.set_preference('useAutomationExtension', False)
service = Service('/usr/local/bin/geckodriver')
driver = webdriver.Firefox(options=options,service=service)
"""
geckodriver_autoinstaller.install()
profile_path = '/Users/doguhanyeke/Library/Application Support/Firefox/Profiles/o399t467.default-release'
options = Options()
options.set_preference('profile', profile_path)
options.set_preference("dom.webdriver.enabled", False)
options.set_preference('useAutomationExtension', False)
desired = DesiredCapabilities.FIREFOX
driver = webdriver.Firefox(options=options, desired_capabilities=desired)
"""
fopen = open("all_package_names", "r")
fopen_w = open("wear_apps_physical", "w")
fopen_w2 = open("wear_apps_virtual", "w")
app_index = 1
paid_app = 0
def execute():
    while True:
        try:
            print("Hi")
            line = fopen.readline()
            if not line:
                break
            packageName = line[:-1]
            global app_index
            print("Index: ", app_index)
            app_index += 1

            domain = "https://play.google.com/store/apps/details?id=" + packageName
            driver.get(domain)
            sleep(4)

            winHandles2 = driver.window_handles
            try:
                # check if the install button is available or not
                install_element = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/c-wiz/div/div/div/div/button')
            except Exception as e:
                # if not found, it throws exception
                continue

            button_element = driver.find_element(By.XPATH,
                                                 '/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/c-wiz/div/div/div/div/button/span')
            # check if the app is free or not
            print("Button text: ", button_element.text)
            if button_element and "Install" not in button_element.text:
                global paid_app
                paid_app += 1
                continue
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                '/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/c-wiz/div/div/div/div/button'))).click()
            sleep(4)

            winHandles = driver.window_handles
            NewWindow = driver.window_handles[0]
            driver.switch_to.window(NewWindow)

            sleep(4)

            iframe = driver.find_element(By.TAG_NAME,"iframe")
            frames = driver.find_elements(By.TAG_NAME, "iframe")
                # switch to selected iframe
            driver.switch_to.frame(frames[2])

            wait.until(EC.element_to_be_clickable((By.XPATH,
                                '/html/body/div/div/div[2]/span/div/div/div[2]/div'))).click()
            sleep(4)
            is_wear_app_physical = False
            is_wear_app_virtual = False
            is_phone_app_physical = False
            is_phone_app_virtual = False
            for i in range(1, 6):
                c = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/span/div/div/div[2]/div/div[2]/div[{}]'.format(str(i)))))

                is_hidden = c.get_attribute("aria-disabled")
                text = c.text
                print("Text: ", text)
                if is_hidden:
                    if "already" not in text:
                        continue

                if "Huawei" in text:
                    is_wear_app_physical = True
                if "gwear" in text:
                    is_wear_app_virtual = True

                if "Pixel" in text:
                    is_phone_app_physical = True
                if "gphone" in text:
                    is_phone_app_virtual = True

            print("Physical w: {}, p: {}".format(is_wear_app_physical, is_phone_app_physical))
            print("Virtual w: {}, p: {}".format(is_wear_app_virtual, is_phone_app_virtual))
            if is_wear_app_physical and is_phone_app_physical:
                print("testable physical: ", packageName)
                fopen_w.write(packageName)
                fopen_w.write("\n")
                fopen_w.flush()
            if is_wear_app_virtual and is_phone_app_virtual:
                print("testable virtual: ", packageName)
                fopen_w2.write(packageName)
                fopen_w2.write("\n")
                fopen_w2.flush()

        except Exception as e:
            print(e)
            continue
        finally:
            print("################")
            global tt
            tt.cancel()
            tt = th.Timer(60, handle)
            tt.start()
            print("timer started!")


tt.start()
print("timer started!")
execute()
tt.cancel()
print("Paid app: ", paid_app)
fopen.close()
fopen_w.close()
fopen_w2.close()