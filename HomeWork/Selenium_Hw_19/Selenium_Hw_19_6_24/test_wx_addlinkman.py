from time import sleep

import allure
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWxlinkname:
    def setup(self):
        print('开始测试')

    @allure.step('删除添加联系人')
    def teardown(self):
        print('结束测试')
        self.driver.find_element(By.XPATH,"//*[text()='lekaixin1']/../..//*[@class='ww_checkbox']").click()
        self.driver.find_element(By.XPATH, "//*[@class='ww_operationBar']//a[text()='删除']").click()
        self.driver.find_element(By.XPATH, "//*[text()='确认']").click()
        self.driver.find_element(By.XPATH, "//*[text()='删除成功']")
        self.driver.close()


    def test_login(self):
        self.opt = webdriver.ChromeOptions()
        self.opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=self.opt)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        with open('cookies.yaml', 'w', encoding='UTF-8') as f:
            yaml.safe_dump(self.driver.get_cookies(), f)


    def test_add_linkname(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        with open('cookies.yaml', 'r', encoding='UTF-8') as f:
            cookies=yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(1)
        self.driver.find_element(By.XPATH,"//*[@class='ww_operationBar']//a[text()='添加成员']").click()
        self.driver.find_element(By.ID,"username").send_keys('lekaixin1')
        self.driver.find_element(By.ID,"memberAdd_english_name").send_keys('kevin1')
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys('lkx1')
        self.driver.find_element(By.XPATH,"//*[text()='男']").click()
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys('17711440200')
        self.driver.find_element(By.ID,"memberAdd_telephone").send_keys('8433053')
        self.driver.find_element(By.ID,"memberAdd_mail").send_keys('260317441@qq.com')
        self.driver.find_element(By.ID,"memberEdit_address").send_keys('地球')
        self.driver.find_element(By.ID,"memberAdd_title").send_keys('测试工程师')
        self.driver.find_element(By.XPATH,"//*[text()='普通成员']").click()
        self.driver.find_element(By.XPATH,"//*[@class='js_member_editor_form']/div[3]/*[@class='qui_btn ww_btn js_btn_save']").click()
        self.driver.find_element(By.XPATH,"//*[text()='保存成功']")
        sleep(5)
