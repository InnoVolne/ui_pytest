#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/12 19:22
"""
import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, StaleElementReferenceException
from common.yaml_config import GetConf
from selenium.webdriver.common.keys import Keys

class ObjectMap:
    url = GetConf().get_url()

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


    def element_to_url(self,
                       url,
                       driver,
                       disappear_locate_type,
                       disappear_locator_expression,
                       appear_locate_type,
                       appear_locator_expression):
        """
        跳转地址
        :param url:
        :param driver:
        :param disappear_locate_type:
        :param disappear_locator_expression:
        :param appear_locate_type:
        :param appear_locator_expression:
        :return:
        """
        try:
            driver.get(self.url + url)
            self.wait_for_read_page_complete(driver)
            self.element_disappear(driver, disappear_locate_type, disappear_locator_expression)
            self.element_appear(driver, appear_locate_type, appear_locator_expression)
            return True
        except Exception as e:
            print("跳转地址出现异常，异常原因：%s" % e)
            return False

    def element_is_display(self, driver, locate_type, locator_expression):
        """
        元素是否显示
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        try:
            driver.fin_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 页面中未出现该元素
            return False


    def element_file_value(self, driver, locate_type, locator_expression, fill_value, timeout = 10):
        """
        元素填值
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param fill_value:
        :param timeout:
        :return:
        """
        try:
            # 元素必须先出现
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            # 清除元素中的值
            element.clear()
        except StaleElementReferenceException:
            self.wait_for_read_page_complete(driver)
            time.sleep(0.06)
            try:
                element = self.element_appear(driver, locate_type, locator_expression, timeout)
                element.clear()
                if type(fill_value) is int or type(fill_value) is float:
                    fill_value = str(fill_value)
                # 填入的值以\n结尾
                if fill_value.endswith("\n"):
                    fill_value = fill_value[:1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_read_page_complete(driver)
                return True
            except StaleElementReferenceException as e:
                raise Exception("元素填值失败,失败原因：%s" % e)
        except Exception:
            raise Exception("元素填值失败,失败原因：%s" % StaleElementReferenceException)

    def element_click(self, driver, locate_type, locator_expression,
                      locate_type_disappear, locator_expression_disappear,
                      locate_type_appear, locator_expression_appear,
                      timeout=30):
        """
        元素点击
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param locate_type_disappear:
        :param locator_expression_disappear:
        :param locate_type_appear:
        :param locator_expression_appear:
        :param timeout:
        :return:
        """
        # 元素是否可见
        element = self.element_appear(driver, locate_type, locator_expression, timeout)
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_read_page_complete(driver)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            element.click()
        except Exception as e:
            raise Exception("页面异常，元素不可点击,原因：%s" % e)
        try:
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear, timeout)
            self.element_appear(driver, locate_type_appear, locator_expression_appear, timeout)
        except Exception as e:
            print("等待元素消失或者出现失败", e)
            return False
        return True


