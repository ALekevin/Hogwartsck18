import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage


class EditMemberPage(BasePage):
    _NAME = (MobileBy.XPATH, "//*[@text='姓名　']/..//android.widget.EditText")
    _PHONE = (MobileBy.XPATH, "//*[@text='手机　']/..//android.widget.EditText")
    _SAVE = (MobileBy.XPATH, "//*[@text='保存']")

    @allure.step('填写添加成员信息')
    def edit_member(self, name, phone):
        from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.add_member_page import AddMemberPage
        self.log_info('填写姓名')
        self.find_and_sendkeys(*self._NAME, name)
        self.log_info('填写手机号')
        self.find_and_sendkeys(*self._PHONE, phone)
        self.log_info('点击保存')
        self.find_and_click(*self._SAVE)
        return AddMemberPage(self.driver)
