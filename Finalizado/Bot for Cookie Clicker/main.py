from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_driver_path = "E:\Codes\Webdev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5
cookie_per_second = driver.find_element_by_id("cps").text

while True:
    cookie.click()

    if time.time() > timeout:
        store = driver.find_elements_by_css_selector("#store div")
        for item in store[::-1]:
            try:
                if not item.get_attribute("class"):
                    item.click()

            except StaleElementReferenceException:
                store = driver.find_elements_by_css_selector("#store div")

        timeout = time.time() + 5
        
        cookie_per_second = driver.find_element_by_id("cps").text
        print(cookie_per_second)

