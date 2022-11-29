import cv2
import numpy

# load an image
img = cv2.imread('dog.jpg', 1)
# resize or scale image
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
# rotate
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# shows image on screen 
cv2.imshow('Image',img)
# closes the window if key is pressed #cv2.destroyAllWindows()
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()

# writes new image file
# cv2.imwrite('new_dog.jpg',img)

print(img) # shows image represenation in matrix form
print(img.shape) # prints dimensions
print(img[257]) # prints pixel row 257 

for i in range(100):
    for j in range(img.shape[1]): # changing pixel values
        img[i][j] = [50,50,50]

cv2.imshow('Image',img)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()

img = cv2.imread('dog.jpg', 1)

tag = img [100:200,300:400]  # copying and pasting parts of image
img[200:300,200:300] = tag

cv2.imshow('Image',img)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()