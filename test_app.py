# ==========writing tests using class============

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-ssl-errors=yes')
# options.add_argument('--ignor-certificate-errors')
#
# driwer = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
#                           options=options)

def save_data(data):
    with open("log.txt", "a") as f:
        f.write(data)


class TestSuite:

    def setup_class(self):
        self.variable = []
        print("test started")


    def teardown_class(self):
        save_data(str(self.variable))
        #print("test finished")

    def setup_method(self):   #preconditions
        save_data('started \n')

    def teardown_method(self):   #postconditions
        save_data("finished \n")

    def test_first_check(self):
        status = requests.get("https://google.com").status_code
        self.variable.append(status)
        assert status == 200

    def test_second_check(self):
        status = requests.get("https://google.com/_").status_code
        self.variable.append(status)
        assert status == 404

    def test_third_check(self):
        status = requests.get("https://wikipedia.com").status_code
        self.variable.append(status)
        assert status == 200
