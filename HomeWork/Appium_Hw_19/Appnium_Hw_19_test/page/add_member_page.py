from time import sleep

from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.base_page import BasePage
from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.full_add_page import FullAddPage


class AddMemberPage(BasePage):
    _MENUAL = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _FULLINPUT = (MobileBy.XPATH, "//*[@text='完整输入']")
    _TOAST = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def goto_full_add_member_page(self):
        self.find_and_click(*self._MENUAL)
        sleep(1)
        try:
            self.find_and_click(*self._FULLINPUT)
        except:
            pass
        sleep(1)
        return FullAddPage(self.driver)

    def get_totals(self):
        result = self.get_toast_text(*self._TOAST)
        return result
