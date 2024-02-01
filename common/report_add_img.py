#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/22 20:40
"""
from time import sleep

import allure
def add_img_to_report(driver, step_name, need_sleep= True):
    """
    截图并插入allure报告
    :param driver: 浏览器驱动
    :param step_name: 步骤名称
    :param need_sleep: 是否等待
    :return:
    """
    if need_sleep:
        sleep(2)
    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)

def add_img_path_to_report(img_path, step_name):
    """
    将图片插入allure报告
    :param img_path: 图片路径
    :param step_name: 步骤名称
    :return:
    """
    allure.attach.file(img_path, step_name, allure.attachment_type.PNG)