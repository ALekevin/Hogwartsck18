from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.base_page import BasePage
from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.contact_list_page import ContactListPage


class MainPage(BasePage):
    _CONTACT = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact_list_page(self):
        self.find_and_click(*self._CONTACT)
        return ContactListPage(self.driver)
