import re
import socket
from urllib.parse import urljoin
import json
import execjs
import requests
import socks

from Helper.DownloadHelper import *
from Helper.ProxyHelper import ProxyHelper

# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)
#socket.socket = socks.socksocket

manga_url = "http://www.dm5.com/manhua-pukuyuri/"

model = MangaDM()

model.set_title("Pukuyuri")
model.parse(manga_url)
model.execute()
# with open('output.json', 'w', encoding='utf-8') as fp:
#     json.dump(model.book, fp)

# print(res)
# model.quit()

# res = model.get_chapter_image_url(page_url)
