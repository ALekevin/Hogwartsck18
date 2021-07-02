from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.basepage import BasePage


class AddMemberPage(BasePage):
    _NAME=(By.ID, "username")
    _ENGLISHNAME=(By.ID, "memberAdd_english_name")
    _USERNAME=(By.ID, "memberAdd_acctid")
    _GENDER=(By.XPATH, "//*[text()='男']")
    _PHONE=(By.ID, "memberAdd_phone")
    _TETEPHONE=(By.ID, "memberAdd_telephone")
    _EMAIL=(By.ID, "memberAdd_mail")
    _ADDRESS=(By.ID, "memberEdit_address")
    _TITLE=(By.ID, "memberAdd_title")
    _POSITION=(By.XPATH, "//*[text()='普通成员']")
    _SAVE=(By.XPATH,"//*[@class='js_member_editor_form']/div[3]/*[@class='qui_btn ww_btn js_btn_save']")
    def add_member_message(self,name,englishname,username,phone,telephone,email,address,title):
        from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.contact_page import ContactPage
        # self.opt = webdriver.ChromeOptions()
        # self.opt.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=self.opt)
        # self.driver.find_element(By.ID, "username").send_keys('lekaixin1')
        self.find(*self._NAME).send_keys(name)
        # self.driver.find_element(By.ID, "memberAdd_english_name").send_keys('kevin1')
        self.find(*self._ENGLISHNAME).send_keys(englishname)
        # self.driver.find_element(By.ID, "memberAdd_acctid").send_keys('lkx1')
        self.find(*self._USERNAME).send_keys(username)
        # self.driver.find_element(By.XPATH, "//*[text()='男']").click()
        self.find_and_click(*self._GENDER)
        # self.driver.find_element(By.ID, "memberAdd_phone").send_keys('17711440200')
        self.find(*self._PHONE).send_keys(phone)
        # self.driver.find_element(By.ID, "memberAdd_telephone").send_keys('8433053')
        self.find(*self._TETEPHONE).send_keys(telephone)
        # self.driver.find_element(By.ID, "memberAdd_mail").send_keys('260317441@qq.com')
        self.find(*self._EMAIL).send_keys(email)
        # self.driver.find_element(By.ID, "memberEdit_address").send_keys('地球')
        self.find(*self._ADDRESS).send_keys(address)
        # self.driver.find_element(By.ID, "memberAdd_title").send_keys('测试工程师')
        self.find(*self._TITLE).send_keys(title)
        # self.driver.find_element(By.XPATH, "//*[text()='普通成员']").click()
        self.find_and_click(*self._POSITION)
        # self.driver.find_element(By.XPATH,
        #                          "//*[@class='js_member_editor_form']/div[3]/*[@class='qui_btn ww_btn js_btn_save']").click()
        self.find_and_click(*self._SAVE)
        # self.driver.find_elements(By.XPATH, "//*[text()='保存成功']")
        # WebDriverWait(self.driver, 5).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='保存成功']")))
        self.wait_for_visibility((By.XPATH, "//*[text()='保存成功']"))
        sleep(5)
        return ContactPage(self.driver)
