import requests


class BaseApi:
    _CORPID = "wwfd58ebdb5647d6c2"
    _CORPSECRET = "PoWW58S7gRXNl0_oZR0lt8nCGwOkPpMpeahpoz0iPyA"
    _BASEURL = "https://qyapi.weixin.qq.com/cgi-bin"

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        r = self.send("GET", f"/gettoken?corpid={self._CORPID}&corpsecret={self._CORPSECRET}")
        return r.json().get("access_token")

    def send(self, method, url, **kwargs):
        url = self._BASEURL + url
        r = requests.request(method, url, **kwargs)
        return r
