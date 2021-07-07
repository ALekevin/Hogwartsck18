import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def log_info(self, message):
        logging.info(message)

    def find(self, by, locator):
        element = self.driver.find_element(by, locator)
        return element

    def finds(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_sendkeys(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def swipe_find(self, text, num=3):
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                element = self.find(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                start_x = int(width * 0.5)
                start_y = int(height * 0.8)
                end_x = int(width * 0.5)
                end_y = int(height * 0.2)
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == (num - 1):
                raise NoSuchElementException(f"找了{i}次 未找到")

    def get_toast_text(self, by, locator):
        result = self.find(by, locator).text
        return result
