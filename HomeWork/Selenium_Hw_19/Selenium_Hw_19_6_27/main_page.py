from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.basepage import BasePage
from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT = (By.ID, 'menu_contacts')

    def gotocontact(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.find_and_click(*self._CONTACT)
        return ContactPage(self.driver)
