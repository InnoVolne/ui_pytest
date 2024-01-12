#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/12 18:23
"""
class LeftMenuBase:
    def level_one_menu(self, menu_name):
        """
        一级菜单栏
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"


    def level_two_menu(self, menu_name):
        """
        二级菜单
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"


if __name__ == '__main__':
    print(LeftMenuBase().level_one_menu('我的订单'))
    print(LeftMenuBase().level_two_menu('已卖出的宝贝'))