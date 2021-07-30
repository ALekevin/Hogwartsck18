import pytest
from faker import Faker

from HomeWork.Appium_Hw_19.Appnium_Hw_19_test.page.app import App


class TestPoFullAddMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main_page()
        # self.faker=Faker("zh_CN")

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.quit()

    def test_po_full_add_member(self, get_datas):
        result = self.main.goto_contact_list_page().goto_add_member_page().goto_full_add_member_page().edit_full_member(
            get_datas[0], get_datas[1]).get_totals()
        assert result == '添加成功'
