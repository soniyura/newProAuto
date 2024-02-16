# ==========writing tests using functions============

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests

@pytest.mark.all
@pytest.mark.slow
def test_request(massage):
    url = "https://google.com"
    resourse = requests.get(url).status_code
    with pytest.raises(ZeroDivisionError):
        var = 1/0
    assert resourse == 200, f"failed with {url}"

@pytest.mark.parametrize("url", ['https://google.com',
                                 'https://vikipedia.com',
                                 'https://wikipedia.com',
                                 'https://google.com/_'])
@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.multy
def test_request_200(url):
    resourse = requests.get(url).status_code
    assert resourse == 200, f"failed with {url}"

@pytest.mark.smoke
@pytest.mark.all
def test_standalone(massage, generator_0):
    assert massage + generator_0 > 250


@pytest.mark.docker_1
def test_selem(docker_run_rm):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignor-certificate-errors')

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              options=options)



    uri_virible = "Napoleon"

    url = ["https://www.wikipedia.org"]

    driver.get(url[0])

    search_field = '//*[@id="searchInput"]'
    element = driver.find_element(By.XPATH, search_field)
    element.send_keys(uri_virible)

    button = '//*[@id="search-form"]/fieldset/button'
    element_button = driver.find_element(By.XPATH, button)
    element_button.click()

    expected_element_path = '//*[@id="firstHeading"]'
    expected_element = driver.find_element(By.XPATH, expected_element_path)

    if expected_element.text == "Napoleon":
        print("successful")
    else:
        print('False')