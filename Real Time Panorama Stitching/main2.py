# import the necessary packages
from Day_10 import Stitcher

import imutils
import cv2

imageA=cv2.imread("Dataset/opencv_aa_2.png")
imageB=cv2.imread("Dataset/opencv_bb_1.png")
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
