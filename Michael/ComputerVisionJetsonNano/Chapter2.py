import cv2
import numpy as np

img = cv2.imread("Resources/apple.jpg") # import image

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to gray scale
imgBlur = cv2.GaussianBlur(imgGray,(7,7), 100)  # cv2.GaussianBlur(image, (Size  of kernal - must be odd numbers), Bluriness)
imgCannay = cv2.Canny(imgBlur, 100, 150) 
kernel = np.ones((5,5), np.uint8)
imgDia = cv2.dilate(imgCannay,kernel, iterations=1)
imgErode = cv2.erode(imgDia,kernel, iterations=1)

cv2.imshow("Image", img)
cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image Blur", imgGray)
cv2.imshow("Image Canny", imgCannay)
cv2.imshow("Image Dia", imgDia)
cv2.imshow("Image Erode", imgErode)
cv2.waitKey(0)
cv2.destroyWindows()