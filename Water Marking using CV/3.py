import numpy as np
import cv2

# read images
original = cv2.imread('Dataset/7.jfif')
mark = cv2.imread('Dataset/watermark.png') 

m,n = original.shape[:2]
print(m,n)

# create overlay image with mark at the upper left corner, use uint16 to hold sum
overlay = np.zeros_like(original, "uint16")
overlay[:mark.shape[0],:mark.shape[1]] = mark


# add the images and clip (to avoid uint8 wrapping)
watermarked = np.array(np.clip(original+overlay, 0, 255), "uint8")

# add some text 5 pixels in from the bottom left
cv2.putText(watermarked, "Watermarking with OpenCV", (5,m-5), cv2.FONT_HERSHEY_PLAIN, fontScale=1.0, color=(255,255,255), thickness=1)

cv2.imshow("original", original)
cv2.imshow("watermarked", watermarked)
cv2.imwrite("watermarked.jpg", watermarked)
cv2.waitKey()
cv2.destroyAllWindows()
