import logging
import pytest

logging.basicConfig(filename="demo_log.log", level= 10)

LOGGER = logging.getLogger()

LOGGER.debug("test started")

# def test_one():
#     LOGGER.info("test started")
#     var1 = 1
#     var2 = 2
#     assert var1 != var2, LOGGER.error(f"Test done with {var1} and {var2}")
#     LOGGER.info("Successfully done")
#
# test_one()

VAR = 10

def fun(variable: int):
    LOGGER.info(f"fun with {VAR} starts")
    return variable + VAR

def test_fub():
    assert fun(19) == 29