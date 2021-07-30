# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
class TestFullAddMember:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "lkx"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def find_swipe(self,text,num=4):
        for i in range(num+1):
            try:
                ele=self.driver.find_element(MobileBy.XPATH,f"//*[@text='{text}']")
                print("找到了")
                return ele
            except:
                if i == num:
                    print(f'找了{i + 1}次，未找到')
                else:
                    size=self.driver.get_window_size()
                    width=size['width']
                    height=size['height']
                    width_start=width/2
                    width_end=width/2
                    height_start=height*0.8
                    height_end=height*0.2
                    duration=2000
                    self.driver.swipe(width_start,height_start,width_end,height_end,duration)


    def test_full_add_member(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.find_swipe('添加成员')
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='完整输入']").click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='姓名　']/../android.widget.EditText").send_keys('hqr')
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys('11011001101')
        self.find_swipe('保存')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(2)
        print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        assert result=='添加成功'
