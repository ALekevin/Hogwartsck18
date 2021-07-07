import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.addresslist_page import AddressListPage
from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage


class MainPage(BasePage):
    _CONTACT = (MobileBy.XPATH, "//*[@text='通讯录']")

    @allure.step('进入通讯录页')
    def goto_addresslist(self):
        self.log_info('进入通讯录页')
        self.find_and_click(*self._CONTACT)
        return AddressListPage(self.driver)
