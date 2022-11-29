import cv2
import numpy

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    # 0,0 indicates top left of screen, 10 represent dot thickness
    # (255,0,0) indicates color
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    # 0,0 indicates top left of rectangle while 200,200 is bottom right
    img = cv2.rectangle(img, (0,0), (200,200), (128,128,128), 5)
    # 60 is the radius, put -1 in the end to fill circle
    img = cv2.circle(img, (100,100), 60, (0,0,255), 10)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Text, then center position, then font, then font scale, then color, then thickness
    img = cv2.putText(img,'Hello World', (10,height-10), font, 2, (0,0,0), 5)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()