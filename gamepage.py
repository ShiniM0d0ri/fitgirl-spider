import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def dlinks(clink):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    options = Options()
    options.add_argument('-headless')

    driver = webdriver.Firefox(firefox_profile=profile, options=options)

    driver.get(clink)
    driver.set_window_size(890, 753)
    
    magnets=driver.find_elements_by_xpath("//a[starts-with(@href, 'magnet:')]")
    print("\nhere are ur magnet links :")
    for magnet in magnets:
        print("\n"+magnet.get_attribute('href'))

    print("\nExiting...")
    driver.quit()


    #magnet=driver.find_element(By.CSS_SELECTOR, ".entry-content > ul:nth-child(5) > li:nth-child(1) > a:nth-child(3)").get_attribute("href")
   # print(magnet)
