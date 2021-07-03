# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddMember:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "lkx"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/cfi").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys('kevin')
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys('17711440200')
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac9").click()
        # sleep(1)
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result1 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成功')]").text
        assert result == "添加成功"
        assert result1 == "添加成功"
