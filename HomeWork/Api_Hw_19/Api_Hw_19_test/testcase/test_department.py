import allure
import pytest

from HomeWork.Api_Hw_19.Api_Hw_19_test.api.department import Department


class TestDepartment:
    def setup(self):
        with allure.step('初始化'):
            self.department = Department()

    def teardown(self):
        pass

    def test_create_department(self, get_datas):
        r = self.department.create_department(get_datas)
        assert r.json().get("errcode") == 0
        assert self.department.is_in_department_id_list(r.json().get('id'))

    def test_update_department(self, get_datas):
        r = self.department.create_department(get_datas)
        result = self.department.update_department(r.json().get("id"))
        assert result.json().get("errcode") == 0
        assert self.department.is_in_department_id_list(r.json().get('id'))

    def test_delete_department(self, get_datas):
        r = self.department.delete_department(self.department.create_department(get_datas).json().get("id"))
        assert r.json().get("errcode") == 0

    def test_get_department_list(self):
        r = self.department.get_department_list()
        print(r.json())
        assert r.json().get("errcode") == 0
