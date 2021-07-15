import json

import mitmproxy.http
from mitmproxy import ctx, http


class HW:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        if "stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url and "_s=" in flow.request.pretty_url:
            ctx.log.info('抓到了request')
            with open("./quote.json", encoding='UTF-8') as f:
                flow.response = http.HTTPResponse.make(
                    200,
                    f.read()
                )

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url and "_s=" in flow.request.pretty_url:
            ctx.log.info("抓到了response")
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["percent"] = 0.00000000001
            data["data"]["items"][1]["quote"]["percent"] = -0.00000000001
            flow.response.text = json.dumps(data)


addons = {
    HW()
}

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
