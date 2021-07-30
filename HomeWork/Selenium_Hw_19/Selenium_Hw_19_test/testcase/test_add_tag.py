import json

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddTag:
    def setup_class(self):
        # option = Options()
        # option.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=option)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # # self.driver.maximize_window()
        # self.driver.implicitly_wait
        pass

    def test_login(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        cookies = str(self.driver.get_cookies())
        with open('./cookies_data.json', 'w', encoding='UTF-8') as f:
            f.write(cookies)

    def test_add_tag(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        with open('./cookies_data.yaml','r',encoding='UTF-8') as f:
            cookies=yaml.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.ID, 'menu_contacts').click()
        self.driver.find_element(By.XPATH, '//*[@class="ww_btnGroup"]/li[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@class="member_colLeft_top_addBtnWrap"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="qui_inputText ww_inputText"]').send_keys('123')
        self.driver.find_element(By.XPATH, '//*[text()="确定"]').click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[text()="创建成功"]')))
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@class="ww_searchInput ww_searchInput_WithAddBtn"]/input')))
        self.driver.find_element(By.XPATH, '//*[@class="ww_searchInput ww_searchInput_WithAddBtn"]/input').send_keys(
            '123')
        total_name = self.driver.find_element(By.XPATH, '//*[@class="ww_searchResult_item_Curr"]/a').text
        assert total_name == '123'
