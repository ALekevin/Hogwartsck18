import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.Selenium_HomeWork_19_6_27.basepage import BasePage
from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.Selenium_HomeWork_19_6_27.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT = (By.ID, 'menu_contacts')

    def gotocontact(self):
        with allure.step('点击通讯录'):
            logging.info('点击通讯录')
            self.find_and_click(*self._CONTACT)
            return ContactPage(self.driver)
