import cv2
import numpy as np
import sys

video = cv2.VideoCapture(0)
bgvideo = cv2.VideoCapture('2.mp4')
sucess, ref_img = video.read()
flag = 0

while True:
    
    sucess, img = video.read()
    if img is not None:
        img = cv2.resize(img , (1500, 850), interpolation= cv2.INTER_AREA)
        ref_img = cv2.resize(ref_img , (1500, 850), interpolation= cv2.INTER_AREA)
        #same Size while comparing
        img = cv2.flip(img, 1)#to avoid webcam issue
        sucess, bg = bgvideo.read()
        bg = cv2.resize(bg , (1500, 850), interpolation= cv2.INTER_AREA)
        #bg img to resizing same size 
        if flag == 0:
            ref_img = img
        
        diff1 = cv2.subtract(img,ref_img)
        diff2 = cv2.subtract(ref_img,img)
        
        diff = diff1 + diff2
        

        diff[abs(diff) < 50] = 0 #try changing the abs value

        gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray[np.abs(gray) <10] = 0

        fgmask = gray.astype(np.uint8)#frontlayer of the video

        fgmask[fgmask > 0 ] = 255

        fgmask_inv = cv2.bitwise_not(fgmask)

        fgimg = cv2.bitwise_and(img, img, mask= fgmask)
        bgimg = cv2.bitwise_and(bg, bg, mask= fgmask_inv)

        dst = cv2.add(bgimg, fgimg)
        cv2.imshow('Video Augmented Reality', dst)

        key = cv2.waitKey(5) & 0xFF

        if ord('q') == key:
            break
        elif ord('d') == key:
            flag = 1
            print("background captured")
        elif ord('r') == key:
            flag = 0
            print("Ready to capture a new background")

cv2.destroyAllWindows()
video.release()
