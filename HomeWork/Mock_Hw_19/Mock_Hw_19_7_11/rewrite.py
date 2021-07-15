import json

import mitmproxy
from mitmproxy import http


class Rewrite:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url and "_s=" in flow.request.pretty_url:
            data = json.loads(flow.response.text)
            print(data)
            data["data"]["items"][0]["quote"]["name"] = "乐恺欣"
            flow.response.text = json.dumps(data)


addons = {
    Rewrite()
}
if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
