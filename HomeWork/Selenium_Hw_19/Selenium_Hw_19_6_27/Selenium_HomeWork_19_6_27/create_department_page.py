import logging
from time import sleep

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.Selenium_HomeWork_19_6_27.basepage import BasePage


class CreateDepartmentPage(BasePage):
    _COMPANYNAME = (By.ID, 'party_name')
    _DEPARTMENTINPUTNAME = (By.XPATH, "//*[text()='部门名称']/..//input[1]")
    _DEPARTMENTSELECT = (By.XPATH, "//*[text()='选择所属部门']")
    _DEPARTMENTNAME = (By.XPATH, "//*[@class='jstree-anchor']")
    _COMMITBTN = (By.XPATH, "//*[text()='确定']")
    _CONTACT = (By.ID, 'menu_contacts')

    def create_department(self, departmentinputname):
        from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.Selenium_HomeWork_19_6_27.contact_page import ContactPage
        sleep(2)
        with allure.step('获取公司名'):
            logging.info('获取公司名')
            company_name = self.find(*self._COMPANYNAME).text
        with allure.step('输入部门名称'):
            logging.info('输入部门名称')
            self.find(*self._DEPARTMENTINPUTNAME).send_keys(departmentinputname)
        with allure.step('选择所属部门'):
            logging.info('选择所属部门')
            self.find_and_click(*self._DEPARTMENTSELECT)
            eles = self.finds(*self._DEPARTMENTNAME)
            print(eles)
            for value in eles:
                if value.text == company_name:
                    value.click()
        with allure.step('点击确定'):
            logging.info('点击确定')
            self.find_and_click(*self._COMMITBTN)
            self.find_and_click(*self._CONTACT)
        return ContactPage(self.driver)