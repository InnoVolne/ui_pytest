#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/11 23:51
"""
class HomeBase:

    def wallet_switch(self):
        """
        首页的钱包开关
        :return:
        """
        return "//div[contains(@class, 'switch')]"

    def logo(self):
        """
        首页左上角的logo
        :return:
        """
        return "//div[contains(text(), '二手')]"

    def welcome(self):
        """
        首页欢迎您回来
        :return:
        """
        return "//span[starts-with(text(), '欢迎您回来')]"