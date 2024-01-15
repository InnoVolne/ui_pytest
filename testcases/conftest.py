#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/15 21:32
"""
import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    global get_driver
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()