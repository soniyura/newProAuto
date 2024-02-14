# https://hub.docker.com/r/selenium/standalone-chrome
# docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
# http://localhost:7900/?autoconnect=1&resize=scale&password=secret

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignor-certificate-errors')

driwer = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)



uri_virible = "Napoleon"

url = ["https://www.wikipedia.org"]

driwer.get(url[0])

search_field = '//*[@id="searchInput"]'
element = driwer.find_element(By.XPATH, search_field)
element.send_keys(uri_virible)

button = '//*[@id="search-form"]/fieldset/button'
element_button = driwer.find_element(By.XPATH, button)
element_button.click()

expected_element_path = '//*[@id="firstHeading"]'
expected_element = driwer.find_element(By.XPATH, expected_element_path)



if expected_element.text == "Napoleon":
    print("successful")
else:
    print('False')




