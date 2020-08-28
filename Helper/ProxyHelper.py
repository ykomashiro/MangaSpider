import requests
from lxml import etree
from bs4 import BeautifulSoup

from Helper.BasicHelper import BasicProxy


class ProxyHelper(BasicProxy):
    def __init__(self):
        super(ProxyHelper, self).__init__()

    def parse(self):
        response = requests.get("http://www.data5u.com/",
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
        try:
            r = requests.head(self.verifyUrl,
                              headers=self.headers,
                              proxies=proxies,
                              timeout=3,
                              verify=False)
            if r.status_code == 200:
                print("{}: success".format(proxy))
                return True
        except:
            pass
        print("{}: fail".format(proxy))
        return False


