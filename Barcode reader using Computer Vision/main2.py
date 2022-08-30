# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import time
import cv2
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
csv = open("barcodes.csv", "w")
found = set()

while True:	
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)		
	for barcode in barcodes:
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
				barcodeData))
			csv.flush()
			found.add(barcodeData)	      	
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF	
	if key == ord("q"):
		break
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
