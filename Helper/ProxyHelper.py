import requests
from bs4 import BeautifulSoup


class ProxyHelper(object):
    def __init__(self):
        self.verifyUrl = 'http://www.baidu.com'
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.r = requests.Session()

    def parse(self):
        response = self.r.get("http://www.data5u.com/",
                              headers=self.headers,
                              timeout=3,
                              verify=False).content
        soup = BeautifulSoup(response, "lxml")
        res = soup.select('ul[class="l2"]')
        print(res[0].get_text())
        for i in res[0].select('span'):
            print(i.get_text())

    def verify(self, ip, port):
        proxy = ':'.join((ip, port))
        proxies = {
            "http": "http://{0}".format(proxy),
            "https": "https://{0}".format(proxy)
        }
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        try:
            r = requests.head(self.verifyUrl,
                              headers=headers,
                              proxies=proxies,
                              timeout=3,
                              verify=False)
            if r.status_code == 200:
                return True
        except:
            pass
        return False


if __name__ == "__main__":
    model = ProxyHelper()
    model.parse()
