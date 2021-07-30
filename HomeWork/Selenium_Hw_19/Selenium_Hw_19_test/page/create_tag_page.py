from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_test.page.base_page import BasePage


class CreateTagPage(BasePage):
    _TAGNAME = (By.XPATH, '//*[@class="qui_inputText ww_inputText"]')
    _COMMIT = (By.XPATH, '//*[text()="确定"]')
    _SUCCUSS_MESSAGE = (By.XPATH, '//*[text()="创建成功"]')

    def create_tag(self, name):
        from HomeWork.Selenium_Hw_19.Selenium_Hw_19_test.page.contact_page import ContactPage
        self.find_and_sendkeys(*self._TAGNAME, name)
        self.find_and_click(*self._COMMIT)
        self.wait_until_by_visibility(*self._SUCCUSS_MESSAGE, 5)
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="创建成功"]')))
        return ContactPage(self.driver)
