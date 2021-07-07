import allure
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage


class EditPersonalPage(BasePage):
    _CONFIRM = (MobileBy.XPATH, "//*[@text='确定']")

    @allure.step('删除成员')
    def delete_personal(self):
        from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.addresslist_page import AddressListPage
        self.log_info('点击删除成员按钮')
        self.swipe_find('删除成员').click()
        self.log_info('点击确定')
        self.find_and_click(*self._CONFIRM)
        return AddressListPage(self.driver)
