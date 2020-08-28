import abc
import requests
import execjs
import os


class BasicMangaDownload:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'Connection': 'keep-alive',
        }
        self.site = ''
        self.cookies = {}
        self.book = {}
        self.book_name = "unkonwn"
        self.chapters_list = []
        self.chapter2url = {}

    @abc.abstractmethod
    def parse(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass

    def search(self):
        pass

    def switch_account(self):
        pass

    def download_single_image(self, image_url, chapter, num):
        save_path = os.path.join(os.getcwd(),
                                 '{0}/{1}'.format(self.book_name, chapter))
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        r = requests.get(image_url, headers=self.headers)
        with open(os.path.join(save_path, "{0}.png".format(num)), 'wb') as f:
            f.write(r.content)

    def add_header(self, key, value):
        self.headers[key] = value

    def add_cookie(self, key, value):
        self.cookies[key] = value

    def set_title(self, name):
        self.book_name = name

    def add_chapter(self, name, index=-1):
        self.chapters_list.insert(index, name)

    def reset_chapter(self):
        self.chapters_list = []

    @property
    def title(self):
        return self.book_name

    @property
    def chapters(self):
        return self.chapters_list

    @staticmethod
    def exec_js(file_path):
        ctx = execjs.compile(open(file_path).read())
        js = 'demo()'
        params = ctx.eval(js)
        return params

    def __len__(self):
        return len(self.chapters_list)

    def __repr__(self):
        origin_str = "《" + self.book_name + "》"
        for chapter in self.chapters_list:
            add_str = "\n  |--" + chapter
            origin_str += add_str
        return origin_str


class BasicProxy:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.verifyUrl = 'http://www.baidu.com'
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }

    @staticmethod
    def verify(ip, port):
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
                return True
        except:
            pass
        return False