import pytest

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_6_27.main_page import MainPage


class TestCase:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize('name,englishname,username,phone,telephone,email,address,title',
                             [['lekaixin1', 'kevin1', 'lkx1', '17711440200', '8433053', '260317441@qq.com', '地球',
                              '测试工程师']])
    def test_add_member(self, name, englishname, username, phone, telephone, email, address, title):
        result=self.main.gotocontact().click_add_member().add_member_message(name, englishname, username, phone, telephone,
                                                                      email, address, title).get_member_name()
        print(result)
        assert name in result