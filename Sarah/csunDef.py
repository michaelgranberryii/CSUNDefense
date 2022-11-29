# Task 1
import cv2 
import random

# Load an Image
img = cv2.imread('somnath.jpg', -1) # -1 = color; 0 = grayscale; 1 = transparency saved

# Resize an Image : let's make Somnath bigger
img = cv2.resize(img, (0, 0), fx = 3, fy = 3) # (0,0) can be pixel size ; fx / fy makes it multiplied by ratio amount

# Rotate an Image : Flip Somnath clockwise
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# store image
cv2.imwrite("flipped_somnath.jpg", img)

# Display an Image
cv2.imshow('Somnath', img)

cv2.waitKey(0) #waits infinitely for a key to be pressed
cv2.destroyAllWindows() #closes out image

# Task 2

# Image Representation
print(img) # image in matrix form

# Value Representing Pixels [blue, green, red] 0 - 255
print(img.shape) # prints (600, 600, 3) = hiegth, width, channel (color vals per pixels)

# Accessing Pixel Values
print(img[257][45:400]) # pixels between 45 and 400 in first row

# Changing Pixel Colors
for i in range(100): # loops through top 100 pixels of image
    for j in range(img.shape[1]): # loops through width of image
        img[i][j] = [random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)] # change to random color vals

cv2.imshow('Colored Somnath', img) #display new image
cv2.waitKey(0) #waits infinitely for a key to be pressed
cv2.destroyAllWindows() #closes out image

# Copying and Pasting parts of an image
tag = img[200:300, 100:400] # copy row 200 - 300, col 100:400
img[100:200, 0:300] = tag # paste to new location

cv2.imshow('Pasted Somnath', img) #display new image
cv2.waitKey(0) #waits infinitely for a key to be pressed
cv2.destroyAllWindows() #closes out image