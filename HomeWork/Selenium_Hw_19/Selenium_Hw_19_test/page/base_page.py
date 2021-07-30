from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver:webdriver=None):
        if driver is None:
            option = Options()
            option.debugger_address = 'localhost:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    def find(self, by, value):
        ele = self.driver.find_element(by, value)
        return ele

    def find_and_click(self, by, value):
        self.driver.find_element(by, value).click()

    def find_and_sendkeys(self, by, value, name):
        self.driver.find_element(by, value).send_keys(name)

    def wait_until_by_visibility(self, by, value, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located((by, value)))
