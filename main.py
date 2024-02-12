import requests
from selenium import webdriver

driwer = webdriver.Remote(command_executor='http://localhost:4444/wd/hab')

uri_virible = "Napoleon"

url = ["https://www.wikipedia.org"]

resource = requests.get(f"{url[0]}{uri_virible}")

data = resource.text

print(data)

element_address = '//*[@id="searchInput"]'
button = '//*[@id="search-form"]/fieldset/button'
