from time import sleep

from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.base_page import BasePage


class FullAddPage(BasePage):
    _ADDNAME = (MobileBy.XPATH, "//*[@text='姓名　']/../android.widget.EditText")
    _ADDPHONE = (MobileBy.XPATH, "//*[@text='手机号']")
    _SAVEBTN = (MobileBy.XPATH, "//*[@text='保存']")

    def edit_full_member(self, name, phone):
        from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.add_member_page import AddMemberPage
        self.find_and_sendkeys(*self._ADDNAME, name)
        self.find_and_sendkeys(*self._ADDPHONE, phone)
        self.find_swipe('保存')
        self.find_and_click(*self._SAVEBTN)
        sleep(1)
        return AddMemberPage(self.driver)
