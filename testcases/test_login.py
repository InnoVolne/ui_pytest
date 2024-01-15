#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/11 22:28
"""

from time import sleep
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestLogin:
    def test_login(self, driver):
        LoginPage().login(driver, "jay")
        sleep(3)



