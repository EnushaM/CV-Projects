#using cv2.putText

import cv2
path = "Dataset/cv.jpg"
image = cv2.imread(path)
window_name = 'Image'
font = cv2.FONT_HERSHEY_SIMPLEX
#font=cv2.FONT_HERSHEY_TRIPLEX
org = (150, 250)
fontScale = 1 # fontScale
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(image, 'hello guys', org, font,
				fontScale, color, thickness, cv2.LINE_AA)


cv2.imshow(window_name, image)
