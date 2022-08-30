# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt #% matplotlib inline


# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade= cv2.CascadeClassifier("haarcascade_smile.xml")


# create a function to detect face
def adjusted_detect_face(img):
	
	face_img = img.copy()
	
	face_rect = face_cascade.detectMultiScale(face_img,scaleFactor = 1.2,minNeighbors = 5)
	
	for (x, y, w, h) in face_rect:
		cv2.rectangle(face_img, (x, y),
					(x + w, y + h), (255, 255, 255), 10)\
		
	return face_img


# create a function to detect eyes
def detect_eyes(img):
	
	eye_img = img.copy()
	eye_rect = eye_cascade.detectMultiScale(eye_img,scaleFactor = 1.2,minNeighbors = 5)
	for (x, y, w, h) in eye_rect:
		cv2.rectangle(eye_img, (x, y),
					(x + w, y + h), (255, 255, 255), 10)	
	return eye_img

# Reading in the image and creating copies
img = cv2.imread('Dataset/index.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

# Detecting the face
face = adjusted_detect_face(img)
plt.imshow(face)
# Saving the image
window_name='face'
cv2.imwrite('Dataset/face.jpg', face)
cv2.imshow(window_name, face)

eyes = detect_eyes(img_copy2)
plt.imshow(eyes)
window_name1='Dataset/eyes.jpg'
cv2.imwrite('Dataset/eyes.jpg', eyes)
cv2.imshow(window_name1, eyes)


eyes_face = adjusted_detect_face(img_copy3)
eyes_face = detect_eyes(eyes_face)
plt.imshow(eyes_face)
window_name2='Dataset/face+eyes.jpg'
cv2.imwrite('Dataset/face+eyes.jpg', eyes_face)
cv2.imshow(window_name2, eyes_face)
