#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/11 23:57
"""
from selenium.webdriver.common.by import By

from base.HomeBase import HomeBase
from base.ObjectMap import ObjectMap


class HomePage(HomeBase, ObjectMap):
    def get_balance(self, driver):
        """
        获取首页的账户余额
        :param driver:
        :return:
        """
        balance_xpath = self.user_balance()
        return self.element_get(driver,By.XPATH, balance_xpath).text
