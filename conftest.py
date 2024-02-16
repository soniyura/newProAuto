import subprocess
import pytest
import requests
from random import randint

@pytest.fixture
def massage():
    print("initial test run") #preconditions
    yield 100
    print('finalization') #postconditions

@pytest.fixture
def generator_0():
    return randint(100, 200)


@pytest.fixture
def docker_run_rm():
    subprocess.run('docker run -d --name selenium_chrome -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest', shell=True, check=True)   #preconditions
    yield
    subprocess.run('docker rm --force selenium_chrome', shell=True, check=True) #postconditions


# docker run -d --name selenium_chrome -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
# docker stop selenium_chrome
# docker rm selenium_chrome
# docker rm --force selenium_chrome      (кил контейнера без стоп)