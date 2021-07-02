from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.add_member_page import AddMemberPage
from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.basepage import BasePage


class ContactPage(BasePage):
    _ADDMEMBER=(By.XPATH,"//*[@class='ww_operationBar']//a[text()='添加成员']")
    _NAMELIST=(By.XPATH,"//*[@class='member_colRight_memberTable_td']/../td[2]")
    def click_add_member(self):
        # self.opt = webdriver.ChromeOptions()
        # self.opt.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=self.opt)
        self.wait_for_click(self._ADDMEMBER)
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='ww_operationBar']//a[text()='添加成员']")))
        self.find_and_click(*self._ADDMEMBER)
        return AddMemberPage(self.driver)

    def get_member_name(self):
        sleep(1)
        Name_List=[]
        eles=self.finds(*self._NAMELIST)
        print(eles)
        for value in eles:
            Name_List.append(value.get_attribute("title"))
        return Name_List
