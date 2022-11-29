# Company: Northridge Defense
# Engineer: Michael Granberry
# Project: Task One and Task Two
# Date 06/23/2022

import cv2
import numpy as np
import random

### Tast One

# Load an image
img = cv2.imread("assets/faces.jpg", -1)

# Resize an image
imgResizeByDiamensions = cv2.resize(img, (640, 480))
imgResizeByScale = cv2.resize(img, (0,0), None, 0.5, 0.5)

# Rotate an image
imageRotate90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
imageRotate180 = cv2.rotate(img, cv2.ROTATE_180)

# Display an image
cv2.imshow("Faces Image", img)
cv2.imshow("Resize Image by Diamensions", imgResizeByDiamensions)
cv2.imshow("Resize Image by Scale", imgResizeByScale)
cv2.imshow("Rotate Image by 90 Clockwise", imageRotate90)
cv2.imshow("Rotate Image by 180", imageRotate180)

#cv2.waitKey(0)
#cv2.destroyAllWindows()





### Task Two

# Image Representation
print(img)

# Value representing pixels
# [ blue green red]

# Accessing pixel values

    # first row
print(img[0])

    # 264th row 60:300
print(img[264][60:300])

# Changing pixel colors
for i in range(50):
    for j in range(img.shape[1]):
        img[i][j] = [random.randrange(255), random.randrange(255), random.randrange(255)]

# Copying and pasting parts of an image
imgMod = cv2.imread("assets/faces.jpg", -1)
tag = imgMod[200:300, 5:45]
imgMod[100:200, 100:140] = tag

# Display an image
cv2.imshow("Change Image Pixels", img)
cv2.imshow("Copy Part of Image", imgMod)

cv2.waitKey(0)
cv2.destroyAllWindows()