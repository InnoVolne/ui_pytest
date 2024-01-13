#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/12 19:22
"""
import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException


class ObjectMap:

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=True):
        """
        单个元素获取
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible: 元素是否必须可见，True 必须可见，False 默认值
        :return: 返回的元素
        """
        # 开始时间
        start_ms = time.time()*1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.fin_element(by=locate_type, value=locator_expression)
                # 如果元素不是必须可见的，直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素必须可见，则需要判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    print(Exception)
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + "定位表达式" + locator_expression)


    def wait_for_read_page_complete(self, driver, timeout = 30):
        """
        判断页面是否加载完成
        :param driver: 浏览器驱动
        :param timeout: 超时时间
        :return: 返回的元素
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 结束时间
        stop_ms = start_ms + (timeout * 1000)
        for i in range(int(timeout * 10)):
            # 查找元素
            try:
                # 获取页面加载状态
                page_state = driver.execte_script("return document.readyState")
                if page_state == "complete":
                    time.sleep(0.01)
                    return True
                else:
                    now_ms = time.time() * 1000
                    # 加载超时
                    if now_ms >= stop_ms:
                        break
                    # 循环加载
                    time.sleep(0.1)
            except WebDriverException:
                # 如果driver有错误，执行js会失败，直接跳过
                time.sleep(0.03)
                return True
        raise Exception("打开页面时，页面元素在%s秒后仍然没有完全加载完" % timeout)


    def  element_disappear(self, driver, locate_type, locator_expression, timeout = 30):
        """
        等待页面元素消失的封装
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return: 返回元素
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.fin_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式：" + locate_type + "\n定位表达式：" + locator_expression)
        else:
            pass


    def element_appear(self, driver, locate_type, locator_expression, timeout = 30):
        """
        等待元素出现
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout: 
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            stop_ms = start_ms + (timeout * 1000)
            for i in range(int(timeout * 1000)):
                try:
                    element = driver.execte_script(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException("元素没有出现，定位方式：" + locate_type + "\n定位表达式：" + locator_expression)
        else:
            pass


