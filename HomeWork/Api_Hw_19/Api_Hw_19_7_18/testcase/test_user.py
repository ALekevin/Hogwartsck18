import logging

import allure
import os, sys
path = os.path.abspath(__file__)
for i in range(5):
  path = os.path.dirname(path)
sys.path.append(path)


from HomeWork.Api_Hw_19.Api_Hw_19_7_18.api.user import USER


@allure.feature('通讯录成员接口测试')
class TestUser:
    def setup_class(self):
        with allure.step('初始化：获取token'):
            logging.info('初始化：获取token')
            self.user = USER()

    @allure.story('创建成员测试')
    def test_create_user(self, get_dates):
        create_user = self.user.create(get_dates[0], get_dates[1], get_dates[2], [1])
        assert create_user.json().get("errcode") == 0

    @allure.story('读取成员测试')
    def test_get_user(self, get_dates):
        self.user.create(get_dates[0], get_dates[1], get_dates[2], [1])
        get_user = self.user.get(get_dates[0])
        assert get_user.json().get("errcode") == 0

    @allure.story('更新成员测试')
    def test_update_user(self, get_dates):
        update_name = "update " + get_dates[1]
        self.user.create(get_dates[0], get_dates[1], get_dates[2], [1])
        update_user = self.user.update(get_dates[0], update_name)
        assert update_user.json().get("errcode") == 0

    @allure.story('删除成员测试')
    def test_delete_user(self, get_dates):
        self.user.create(get_dates[0], get_dates[1], get_dates[2], [1])
        delete_user = self.user.delete(get_dates[0])
        assert delete_user.json().get("errcode") == 0
