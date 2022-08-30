import pyqrcode 
from pyqrcode import QRCode
surl = "https://in.pinterest.com/"
url = pyqrcode.create(surl)
url.svg("test.svg", scale = 8)
url.png('test.png', scale=8)
