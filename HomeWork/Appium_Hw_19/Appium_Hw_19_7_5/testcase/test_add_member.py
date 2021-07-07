import allure
from faker import Faker

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.app import App


class TestAddMember:
    def setup_class(self):
        self.faker = Faker('zh_CN')
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        # self.app.restart()
        self.app.back()

    def teardown_class(self):
        self.app.quit()

    @allure.feature('添加成员')
    def test_add_member(self):
        with allure.step('构造虚拟数据'):
            name = self.faker.name()
            phone = self.faker.phone_number()
        with allure.step('执行用例'):
            result = self.main.goto_addresslist().goto_addmember_page().goto_edit_member_page(). \
                edit_member(name, phone).get_result()
            assert '添加成功' == result
