import requests

from HomeWork.Api_Hw_19.Api_Hw_19_test.api.base_api import BaseApi


class Department(BaseApi):
    def create_department(self, name, parentid=1, **kwargs):
        """
        创建部门
        必填项：name,parentid
        非必填项:name_en,order,id
        :return: response
        """
        data = {
            "name": name,
            "parentid": parentid
        }
        data.update(kwargs)
        r = self.send("POST", f"/department/create?access_token={self.get_token()}", json=data)
        return r

    def update_department(self, ID, **kwargs):
        """
        更新部门
        必填项：ID
        非必填项:name,name_en,parentid,order
        :return: response
        """
        data = {
            "id": ID
        }
        data.update(kwargs)
        r = self.send("POST", f"/department/update?access_token={self.get_token()}", json=data)
        return r

    def delete_department(self, ID):
        """
        删除部门
        必填项：ID
        :return:
        """
        r = self.send("GET", f"/department/delete?access_token={self.get_token()}&id={ID}")
        return r

    def get_department_list(self, ID=None):
        """
        获取部门列表
        :param ID:
        非必填项:ID
        :return:
        """
        r = self.send("GET", f"/department/list?access_token={self.get_token()}&id={ID}")
        return r

    def is_in_department_id_list(self, id):
        """
        判断部门id是否在部门列表中（判断是否添加部门成功）
        :param id: 部门id
        :return: True：添加成功 False：添加失败
        """
        department_list = self.get_department_list().json().get("department")
        for list in department_list:
            if id == list.get("id"):
                return True
        return False
