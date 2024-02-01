#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/11 22:28
"""

from time import sleep

import allure
import pytest

from page.LoginPage import LoginPage
from common.report_add_img import add_img_to_report


class TestLogin:
    @pytest.mark.login
    @allure.feature("登录成功")
    @allure.description("登录成功")
    def test_login(self, driver):
        """
        使用正确的账号登录
        :param driver:
        :return:
        """
        with allure.step("登录成功测试"):
            LoginPage().login(driver, "jay")
            sleep(3)

    @pytest.mark.login
    @allure.feature("登录失败")
    @allure.description("登录失败")
    def test_login_failure(self, driver):
        """
        使用错误的账号登录
        :param driver:
        :return:
        """
        with allure.step("登录失败测试"):
            LoginPage().login(driver, "failure")
            sleep(3)
            add_img_to_report(driver, "登录失败")




