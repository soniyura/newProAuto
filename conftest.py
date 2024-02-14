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