import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from HomeWork.Selenium_Hw_19.Selenium_Hw_19_test.page.main_page import MainPage


class TestPoAddTag:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize('name', ['123','hqr'])
    def test_po_add_tag(self, name):
        result = self.main.goto_contact_page().goto_create_tag_page().create_tag(name).get_tag_name(name)
        assert result == name
