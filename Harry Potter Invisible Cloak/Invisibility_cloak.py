import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0
for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)

while (cap.isOpened()):
    ret, img = cap.read()

    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value, 0)
    lower_green = np.array([26,65,26])
    upper_green= np.array([90,255,255])
    mask1 = cv2.inRange(hsv, lower_green, upper_green)

    lower_green1 = np.array([170,120,70])
    upper_green1 = np.array([179,113,102])    
    mask2 = cv2.inRange(hsv, lower_green1, upper_green1)

    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv2.imshow('Display', img)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
