#! /usr/bin/python3
# coding=utf-8
# @Time: 2024/1/11 2:40 PM
# @Author: sophie
from time import  sleep
from config.driver_config import DriverConfig

driver = DriverConfig().driver_config()
driver.get("http://192.168.1.5")
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(3)
driver.quit()
