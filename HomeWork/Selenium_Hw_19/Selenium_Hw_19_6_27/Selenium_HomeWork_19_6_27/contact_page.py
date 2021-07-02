import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.Selenium_HomeWork_19_6_27.basepage import BasePage
from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.Selenium_HomeWork_19_6_27.create_department_page import \
    CreateDepartmentPage


class ContactPage(BasePage):
    _ADDBTN = (By.CLASS_NAME, "member_colLeft_top_addBtn")
    _ADDDEPARTMENT = (By.XPATH, "//*[text()='添加部门']")
    _SEARCH = (By.ID, "memberSearchInput")
    _NAME = (By.XPATH, "//*[@class='ww_commonImg ww_commonImg_TreeMenuThumb']/../a")
    _FAILMESSAGE = (By.XPATH, "//*[text()='该部门已存在']")
    _DEPARTMENTBTN = (By.XPATH, "//*[@class='jstree-anchor']/*[@class='icon jstree-contextmenu-hover']")
    _DELETEBTN = (By.XPATH, "//*[text()='删除']")
    _COMMITBTN = (By.XPATH, "//*[text()='确定']")
    _DELETEMESSAGE = (By.XPATH, "//*[text()='删除部门成功']")

    def click_add_department(self):
        with allure.step('点击添加按钮'):
            logging.info('点击添加按钮')
            self.find_and_click(*self._ADDBTN)
        with allure.step('点击添加部门按钮'):
            logging.info('点击添加部门按钮')
            self.find_and_click(*self._ADDDEPARTMENT)
        return CreateDepartmentPage(self.driver)

    def get_department_name(self, name):
        with allure.step('查询框输入部门名称'):
            logging.info('查询框输入部门名称')
            self.find(*self._SEARCH).send_keys(name)
            result = self.find(*self._NAME).text
            return result

    def get_same_fail_message(self):
        with allure.step('获取失败信息'):
            logging.info('获取失败信息')
            self.find(*self._FAILMESSAGE)
