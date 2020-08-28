import os
import re
import requests
import execjs
import selenium
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.Config import *
from Helper.BasicHelper import BasicMangaDownload


def download_image(url, name, num):
    save_path = os.path.join(os.getcwd(), 'Data/{0}'.format(name))
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    r = requests.get(url)
    with open('Data/{0}/{1}.png'.format(name, num), 'wb') as f:
        f.write(r.content)


class MangaDM(BasicMangaDownload):
    def __init__(self):
        super(MangaDM, self).__init__()
        self.site = 'http://m.dm5.com/'
        """
        [
            'chapter_1':[
                (page, image_url),
                (page, image_url),
            ],
            'chapter_2':[
                (page, image_url),
                (page, image_url),
            ]
        ]
        """

    def parse(self, url):
        self.get_chapter_list(url)
        for item in self.chapter2url.items():
            image_urls = self.get_chapter_image_url(item[1])
            self.book[item[0]] = list(enumerate(image_urls))

    def execute(self):
        for item in self.book.items():
            self.add_header('Referer', self.chapter2url[item[0]])
            for page, image_url in item[1]:
                print(item[0], page)
                self.download_single_image(image_url, item[0], page)

    def search(self, key_word):
        pass

    def get_chapter_list(self, url):
        res = requests.get(url)
        res.encoding = "utf-8"
        root = etree.HTML(res.content)

        urls = []

        items = root.xpath(
            '//div[@id="chapterlistload"]/ul/li/a[@href]/text()')
        for item in items:
            name = str(item).strip()
            if name != '':
                self.chapters_list.append(name)
        items = root.xpath('//div[@id="chapterlistload"]/ul/li/a/@href')
        for item in items:
            name = str(item).strip()
            if name != '':
                urls.append(urljoin(self.site, name))
        self.chapter2url = dict(zip(self.chapters_list, urls))
        print(self.chapter2url)

    def get_chapter_image_url(self, url):
        res = requests.get(url)
        res.encoding = 'utf-8'
        root = etree.HTML(res.content)
        items = root.xpath("//script/text()")
        for item in items:
            item = str(item)
            if item.startswith("eval"):
                item = item.strip()
                MangaDM.write_js("test.js", item)
                result = MangaDM.exec_js("test.js")
                return result

    @staticmethod
    def write_js(file_path, js_str):
        with open(file_path, 'w') as fn:
            js_func = "function demo() {" + js_str + "; return newImgs;}"
            fn.write(js_func)
