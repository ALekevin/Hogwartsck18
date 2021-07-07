import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.add_member_page import AddMemberPage
from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage
from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.personal_information_page import PersonalInformationPage


class AddressListPage(BasePage):
    _PERSONAL = (MobileBy.XPATH,
                 "//android.widget.ListView/android.widget.RelativeLayout//android.view.ViewGroup/android.widget.TextView")

    @allure.step('点击添加成员')
    def goto_addmember_page(self):
        self.log_info('滑动查找添加成员按钮')
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    @allure.step('点击成员')
    def click_member(self, name):
        # _MEMBERNAME = (MobileBy.XPATH, f'//*[@text={name}]')
        self.log_info(f'点击成员:{name}')
        self.swipe_find(name).click()
        return PersonalInformationPage(self.driver)

    @allure.step('获取成员元素列表')
    def get_personals(self):
        self.log_info('获取成员列表')
        result = self.finds(*self._PERSONAL)
        return result
