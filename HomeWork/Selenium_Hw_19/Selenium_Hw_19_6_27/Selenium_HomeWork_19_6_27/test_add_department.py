import allure
import pytest
import yaml

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.Selenium_HomeWork_19_6_27.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass
        # self.main.close_driver()

    @allure.feature('添加部门成功')
    def test_add_department(self, get_deparment_name):
        result = self.main.gotocontact().click_add_department().create_department(
            get_deparment_name).get_department_name(get_deparment_name)
        print(result)
        assert get_deparment_name == result

    @allure.feature('添加部门失败')
    def test_fail_add_department(self, get_deparment_name):
        self.main.gotocontact().click_add_department().create_department(
            get_deparment_name).click_add_department().create_department(get_deparment_name).get_same_fail_message()
