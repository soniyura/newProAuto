# ==========writing tests using functions============


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