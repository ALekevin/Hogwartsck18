import requests


class BaseApi:
    _CORPID = "wwfd58ebdb5647d6c2"
    _CORPSECRET = "PoWW58S7gRXNl0_oZR0lt8nCGwOkPpMpeahpoz0iPyA"
    _BASEURL="https://qyapi.weixin.qq.com/cgi-bin"

    def get_token(self):
        """
        获取token值
        :return: token
        """
        r = self.send("GET",f"/gettoken?corpid={self._CORPID}&corpsecret={self._CORPSECRET}")
        return r.json().get('access_token')

    def send(self, method, url, **kwargs):
        """
        封装requests请求的方法
        :param method: 请求方式
        :param url: 请求路径
        :return:
        """
        url = self._BASEURL + url
        r = requests.request(method, url, **kwargs)
        return r