import urllib.request
import cv2
import numpy as np
import imutils

url='http://192.168.1.15:8080/shot.jpg'
#url='http://25.87.123.168:8080/shot.jpg'
while True:
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
    # it is mainly used to recover images from network transmission data
    img = cv2.imdecode(imgNp, -1)
    img = imutils.resize(img, width=450)
    cv2.imshow("CameraFeed",img)
    k = cv2.waitKey(1)
    if k%256 == 27:
           # ESC pressed
           print("Escape hit, closing...")
           break
    elif k%256 == 32:
            # SPACE pressed
            img_name = "captured_image.jpg"
            cv2.imwrite(img_name, img)
            print("image saved")
            
'''
            cam.release()
            cv2.destroyAllWindows()'''
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText(img_name)
print(info)

file = open("result.txt","w")
file.write(info)
file.close()
print("Written Successful")
