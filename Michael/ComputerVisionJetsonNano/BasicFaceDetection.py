import cv2

img = cv2.imread("../Resources/group.JPG") # import image

faceCascade = cv2.CascadeClassifier("../Resources/haarcascade_frontalface_default.xml") # import face detection classifier file
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to gray scale
faceObjects = faceCascade.detectMultiScale(imgGray, 1.3 ,4) # find face objects in image - detectMultiScale(image, scale factor, minimum neighbors)

for (x, y, w, h) in faceObjects: # draw box around faces
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 6)
cv2.imshow("Output", img)
cv2.waitKey(0)