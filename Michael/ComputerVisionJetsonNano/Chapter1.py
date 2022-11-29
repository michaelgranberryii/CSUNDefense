import cv2

### Importing an image
# img = cv2.imread("Resources/apple.jpg") # import image
# cv2.imshow("Output", img) # Show title cv2.imshow("Image title", image)
# cv2.waitKey(0) # waitKey = wait forever

### Import Video
# from cv2 import imshow 
# from cv2 import waitKey
# frameWidth = 640 # video image width
# frameHeight = 480 # video image height

# cap = cv2.VideoCapture("Resources/test.mp4") # import video

# while True:
#     success, img = cap.read() # returnss boolean AND image frame
#     img = cv2.resize(img,(frameWidth, frameHeight)) # resize image
#     cv2.imshow("Result", img)  # show image
#     if cv2.waitKey(1) & 0xFF == ord('q'): # break out of program
#         break


### Run Webcam
from cv2 import imshow
from cv2 import waitKey
frameWidth = 1920 # webcam video width
frameHeight = 1080 # webcam video height

cap = cv2.VideoCapture(2) # import video from MacBook webcam

while True:
    success, img = cap.read() # returns boolean AND image frame
    img = cv2.resize(img,(frameWidth, frameHeight)) # resize image
    cv2.imshow("Result", img)  # show image
    if cv2.waitKey(1) & 0xFF == ord('q'): # break out of program
        break