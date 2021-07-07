import pytest
from faker import Faker

from HomeWork.Appium_Hw_19.Appium_Hw_19_7_5.page.app import App


class TestDeletePersonal:
    def setup_class(self):
        self.faker = Faker('zh_CN')
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        self.app.back(1)

    def teardown_class(self):
        self.app.quit()

    @pytest.mark.parametrize('name', ['朱宇'])
    def test_delete_personal(self, name):
        result = self.main.goto_addresslist().click_member(name) \
            .goto_set_information().goto_edit_member().delete_personal().get_personals()
        for value in result:
            assert not value.text == name