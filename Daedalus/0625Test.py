import cv2
import numpy

# first, load our image 
img = cv2.imread('team1a.jpg',1)

#rotate an image 
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# we kinda stuck, so press q to quit 
cv2.imshow('Team Photo :)', img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
