import cv2
import numpy as np

img = cv2.imread("Resources/apple.jpg")
print(img.shape)

imgResizeByDiamensions = cv2.resize(img,(640, 480))
imgResizeByScale = cv2.resize(img,(0,0), None, 0.5,0.5)

imgCrop = img[100:200,200:300]

cv2.imshow("Image", img)
cv2.imshow("Image Resize By", imgResizeByDiamensions)
cv2.imshow("Image Resize By Sacle", imgResizeByScale)
cv2.imshow("Image Crop", imgCrop)
cv2.waitKey(0)
cv2.destroyWindows()