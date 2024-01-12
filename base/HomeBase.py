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

    def show_data(self):
        """
        同级元素的下一个元素
        我的日历
        :return:
        """

        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        """
        同级元素的上一级元素
        首页头像
        :return:
        """
        return "//span[contains(text(), '欢迎')]/parent::div/preceding-sibling::div"

    def home_user_avatar2(self):
        """
        xpath轴之ancestor（祖先）
        首页头像
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class, 'user_avatar')]"