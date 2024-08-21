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

# output:
# 0 if it is paid app
#
def download_and_extract_apk(package_name):
    domain = "https://play.google.com/store/apps/details?id=" + package_name
    with webdriver.Firefox() as driver:
        try:
            # open app page in play store
            driver.get(domain)

            # click install if it is free app
            wait = WebDriverWait(driver, 5)
            text = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/c-wiz/div/div/div/div/button/span/span")\
                .get_attribute("text")
            if text != "Install":
                # paid app, exit the function
                return 0

            wait.until(EC.element_to_be_clickable((By.XPATH,
                    "/html/body/c-wiz[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/c-wiz/div/div/div/div/button/span/span"))).click()
            

            element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, "// *[ @ id = \"yw0\"] / li[{}] / div / div / h4[1] / a".format(str(index)))))
            element.click()
        except Exception as e:
            print(e)


            """
            app_list = []
            fopen = open("app_list", "w")
            # keep only unique package names
            package_name_set = set()
            fopen2 = open("package_name_set", "w")
            li_index = 1
            for i in range(1,93):
                driver.get(url+str(i))


                form = driver.find_element(By.XPATH, "//*[@id=\"yw0\"]")
                li_list = form.find_elements(By.CLASS_NAME, "span2")
                size = len(li_list)
                for index in range(1, size+1):
                    flag = 0
                    try:
                        driver.get(url + str(i))

                        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                            (By.XPATH, "// *[ @ id = \"yw0\"] / li[{}] / div / div / h4[1] / a".format(str(index)))))
                        element.click()
                        flag = 1
                        app_dict = {}
                        # app_name
                        app_name = driver.find_element(By.XPATH, "// *[ @ id = \"content\"] / div / div[1] / div[2] / table / tbody / tr[1] / td / h1").text
                        app_dict["app_name"] = app_name
                        print(app_name)
                        # developer
                        developer = driver.find_element(By.XPATH, "// *[ @ id = \"content\"] / div / div[1] / div[2] / table / tbody / tr[2] / td / h1 / small").text
                        app_dict["developer"] = developer
                        print(developer)
                        # app_information
                        app_info = driver.find_element(By.XPATH, "// *[ @ id = \"content\"] / div / div[1] / div[2] / table / tbody / tr[3] / td").text
                        app_dict["app_info"] = app_info
                        print(app_info)
                        # link
                        link = driver.find_element(By.XPATH, "// *[ @ id = \"content\"] / div / div[1] / div[2] / table / tbody / tr[4] / td / a").get_attribute("href")
                        app_dict["link"] = link
                        print(link)

                        response = request.urlopen(link)
                        new_url = response.url

                        if response.code == 200 and new_url:
                            package_name = new_url[new_url.rfind("=") + 1:]
                            app_dict["package_name"] = package_name
                            print(package_name)

                            if package_name not in package_name_set:
                                package_name_set.add(package_name)
                                fopen2.write(package_name)
                                fopen2.write("\n")

                            app_list.append(app_dict)
                            #json_object = json.dumps(app_dict, indent=4)
                    except Exception as e:
                        print(e)
                        print("except")

                    finally:
                        # go back
                        if flag:
                            driver.back()


                    print("a")
            """