from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    def __init__(self, driver: webdriver=None):
        self.driver = driver

    def find_swipe(self, text, num=4):
        for i in range(num + 1):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                print("找到了")
                return ele
            except:
                if i == num:
                    print(f'找了{i + 1}次，未找到')
                else:
                    size = self.driver.get_window_size()
                    width = size['width']
                    height = size['height']
                    width_start = width / 2
                    width_end = width / 2
                    height_start = height * 0.8
                    height_end = height * 0.2
                    duration = 2000
                    self.driver.swipe(width_start, height_start, width_end, height_end, duration)

    def find(self, by, value):
        ele = self.driver.find_element(by, value)
        return ele

    def find_and_click(self, by, value):
        self.find(by, value).click()

    def find_and_sendkeys(self, by, value, text):
        self.find(by, value).send_keys(text)

    def get_toast_text(self, by, value):
        toast = self.find(by, value).get_attribute('text')
        return toast
