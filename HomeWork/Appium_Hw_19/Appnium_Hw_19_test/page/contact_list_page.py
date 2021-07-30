from time import sleep

from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.add_member_page import AddMemberPage
from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.base_page import BasePage


class ContactListPage(BasePage):
    _ADDMEMBERBTN=(MobileBy.XPATH, "//*[@text='添加成员']")
    def goto_add_member_page(self):
        self.find_swipe('添加成员')
        self.find_and_click(*self._ADDMEMBERBTN)
        sleep(1)
        return AddMemberPage(self.driver)
