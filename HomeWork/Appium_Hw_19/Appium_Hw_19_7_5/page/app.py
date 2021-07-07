import allure
from appium import webdriver

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.basepage import BasePage
from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.main_page import MainPage


class App(BasePage):
    @allure.step('初始化app')
    def start(self):
        if self.driver == None:
            with allure.step('driver为空，初始化driver'):
                print('driver == None')
                caps = {}
                caps["platformName"] = "Android"
                caps["appPackage"] = "com.tencent.wework"
                caps["appActivity"] = ".launch.LaunchSplashActivity"
                caps["deviceName"] = "lkx"
                caps["noReset"] = "true"
                caps["ensureWebviewsHavePages"] = True
                self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
                self.driver.implicitly_wait(5)
        else:
            with allure.step('driver存在，复用driver'):
                print('driver != None')
                self.driver.launch_app()
        return self

    @allure.step('重启app')
    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    @allure.step('回退关闭app')
    def back(self, num=3):
        for i in range(num):
            self.driver.back()

    @allure.step('关闭app')
    def quit(self):
        self.driver.quit()

    @allure.step('进入主页面')
    def goto_main_page(self):
        return MainPage(self.driver)
