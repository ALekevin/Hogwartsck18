from appium import webdriver

from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.base_page import BasePage
from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver==None:
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "lkx"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def back(self, num=3):
        for i in range(num):
            self.driver.back()

    def quit(self):
        self.driver.quit()

    def goto_main_page(self):
        return MainPage(self.driver)
