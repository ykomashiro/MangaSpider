import re
import socket
from urllib.parse import urljoin
import json
import execjs
import requests
import socks
import sys, os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

from Plugin.MangaDM import *
from Helper.ProxyHelper import ProxyHelper

manga_url = "http://www.dm5.com/manhua-pukuyuri/"

model = MangaDM()

model.set_title("Pukuyuri")
model.parse(manga_url)
model.execute()