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
    def test_login(self):
        driver = DriverConfig().driver_config()
        driver.get("http://192.168.1.5")
        sleep(3)
        LoginPage().login_input_value(driver, "用户名", "周杰伦")
        sleep(1)
        LoginPage().login_input_value(driver, "密码", "123456")
        sleep(1)
        LoginPage().click_login(driver, "登录")
        sleep(3)
        driver.quit()

    def test_login2(self):
        print("test2")