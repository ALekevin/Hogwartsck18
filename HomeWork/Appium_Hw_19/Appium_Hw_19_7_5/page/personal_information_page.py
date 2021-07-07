import allure
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage
from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.set_information_page import SetInformationPage


class PersonalInformationPage(BasePage):
    _SETBTN = (
        MobileBy.XPATH, "//*[@text='个人信息']/../../../../../android.widget.LinearLayout[2]//android.widget.TextView")

    @allure.step('点击设置按钮')
    def goto_set_information(self):
        self.log_info('点击设置按钮')
        self.find_and_click(*self._SETBTN)
        return SetInformationPage(self.driver)
