import pyqrcode 
from pyqrcode import QRCode
surl = "https://www.pantechsolutions.net/computer-vision-crash-course/"
url = pyqrcode.create(surl)
url.svg("test.svg", scale = 8)
url.png('test.png', scale=8)
