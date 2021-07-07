import allure
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage
from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.edit_personal_page import EditPersonalPage


class SetInformationPage(BasePage):
    _EDITMEMBER = (MobileBy.XPATH, "//*[@text='编辑成员']")

    @allure.step('点击编辑成员按钮')
    def goto_edit_member(self):
        self.log_info('点击编辑成员按钮')
        self.find_and_click(*self._EDITMEMBER)
        return EditPersonalPage(self.driver)
