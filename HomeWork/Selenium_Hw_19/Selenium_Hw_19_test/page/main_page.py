from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_test.page.base_page import BasePage
from HomeWork.Selenium_Hw_19.Selenium_Hw_19_test.page.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT = (By.ID, 'menu_contacts')

    def goto_contact_page(self):
        self.find_and_click(*self._CONTACT)
        return ContactPage(self.driver)
