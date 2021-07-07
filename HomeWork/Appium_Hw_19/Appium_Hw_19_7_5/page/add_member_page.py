import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage
from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.edit_member_page import EditMemberPage


class AddMemberPage(BasePage):
    _MENUAL = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _TOAST = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    @allure.step('点击手动输入添加')
    def goto_edit_member_page(self):
        self.log_info('点击手动输入添加')
        self.find_and_click(*self._MENUAL)
        return EditMemberPage(self.driver)

    @allure.step('获取toast提示信息')
    def get_result(self):
        self.log_info('获取toast提示信息')
        result = self.get_toast_text(*self._TOAST)
        return result
