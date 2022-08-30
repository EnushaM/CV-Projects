# import the opencv library
import cv2
# define a video capture object
vid = cv2.VideoCapture(1)
img_counter=0
while(True):
        ret, frame = vid.read()
        # Display the resulting fram
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
                print("Escape hit, closing...")
                break
        elif k%256 == 32:
                # SPACE pressed
                img_name = "opencv_bb_{}.png".format(img_counter)
                #cv2.imwrite(img_name, frame)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
