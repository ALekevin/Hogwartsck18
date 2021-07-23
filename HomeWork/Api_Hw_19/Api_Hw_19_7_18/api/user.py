from HomeWork.Api_Hw_19.Api_Hw_19_7_18.api.base_api import BaseApi


class USER(BaseApi):

    def create(self, userid, name, mobile, department, **kwargs):
        """
        创建成员
        :param token:
        :param kwargs:
        :return:
        """
        json = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        json.update(kwargs)
        r = self.send("POST", f"/user/create?access_token={self.token}", json=json)
        return r

    def get(self, userid):
        """
        获取成员信息
        :param token:
        :param userid:
        :return:
        """
        r = self.send("GET", f"/user/get?access_token={self.token}&userid={userid}")
        return r

    def update(self, userid, name, **kwargs):
        """
        更新成员信息
        :param token:
        :return:
        """
        json = {
            "userid": userid,
            "name": name
        }
        json.update(kwargs)
        r = self.send("POST", f"/user/update?access_token={self.token}", json=json)
        return r

    def delete(self, userid):
        """
        删除成员
        :param userid:
        :return:
        """
        r = self.send("GET", f"/user/delete?access_token={self.token}&userid={userid}")
        return r
