import os

import requests
from bs4 import BeautifulSoup

from Config.Config import *


def download_image(url, name, num):
    save_path = os.path.join(os.getcwd(), 'Data/{0}'.format(name))
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    r = requests.get(url, headers=HEADERS[0])
    with open('Data/{0}/{1}.png'.format(name, num), 'wb') as f:
        f.write(r.content)

class MangaDB(object):
    def __init__(self):
        pass
    

