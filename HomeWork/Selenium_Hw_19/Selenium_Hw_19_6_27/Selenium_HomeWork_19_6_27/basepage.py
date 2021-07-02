from selenium import webdriver


class BasePage:
    def __init__(self, driver_base: webdriver = None):
        if driver_base == None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        else:
            self.driver = driver_base

    def find(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator):
        eles = self.driver.find_elements(by, locator)
        return eles

    def find_and_click(self, by, locator):
        ele = self.driver.find_element(by, locator)
        ele.click()

    def close_driver(self):
        self.driver.close()
