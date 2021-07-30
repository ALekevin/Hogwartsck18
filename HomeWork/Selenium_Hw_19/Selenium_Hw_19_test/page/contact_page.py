from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_test.page.base_page import BasePage
from HomeWork.Selenium_Hw_19.Selenium_Hw_19_test.page.create_tag_page import CreateTagPage


class ContactPage(BasePage):
    _TAG = (By.XPATH, '//*[@class="ww_btnGroup"]/li[2]/a')
    _ADDTAG = (By.XPATH, '//*[@class="member_colLeft_top_addBtnWrap"]')
    _SEARCHINPUT = (By.XPATH, '//*[@class="ww_searchInput ww_searchInput_WithAddBtn"]/input')
    _SEARCHTAGNAME = (By.XPATH, '//*[@class="ww_searchResult_item_Curr"]/a')

    def goto_create_tag_page(self):
        self.find_and_click(*self._TAG)
        self.find_and_click(*self._ADDTAG)
        return CreateTagPage(self.driver)

    def get_tag_name(self, name):
        self.wait_until_by_visibility(*self._SEARCHINPUT, 5)
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@class="ww_searchInput ww_searchInput_WithAddBtn"]/input')))
        self.find_and_sendkeys(*self._SEARCHINPUT, name)
        total_name = self.find(*self._SEARCHTAGNAME).text
        return total_name
