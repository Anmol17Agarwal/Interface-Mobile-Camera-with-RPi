import urllib.request
import cv2
import numpy as np
import imutils
url='http://192.168.1.9:8888/shot.jpg'
while True:
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    img = imutils.resize(img, width=450)
    cv2.imshow("ASUS",img)
    if ord('q') ==  cv2.waitKey(1):# if condition to exit the program
        exit(0)
