from Helper.DownloadHelper import *

import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)
socket.socket = socks.socksocket
print(requests.get('http://ifconfig.me/ip').text)
