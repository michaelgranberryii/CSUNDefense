import cv2
import numpy

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    # convert BGR to Hue Saturation
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = numpy.array([90,50,50]) # light blue
    upper_blue = numpy.array([130,255,255]) # dark blue

    # will black out any values outside the lower and upper range
    # basically will only show blue colors in theory
    mask = cv2.inRange(hsv,lower_blue,upper_blue) # is only 0s and 1s
    result = cv2.bitwise_and(frame,frame,mask=mask) # gives color
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(result,'Blue Detector', (10,height-10), font, 2, (255,0,0), 5)


    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()