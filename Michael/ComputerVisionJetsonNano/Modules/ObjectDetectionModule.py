"""
Oject detection Module
Viola Jhones Method

Engineer: Michael Granberry
Company: CSUN Defense
Date: 07/07/22
"""
import cv2

def findObjects(img, objectCascade, scaleF = 1.1, minN = 4):
    """
    finds ojects using the haarcascade file

    :param img: Image in which the objects need to be found
    :param objectCasace: Object casade created with Casade Classifier
    :param scaleF: how much the image size is reduced at each image scale
    :param minN: how many neighbors each rectagle should have to accept as valid
    :return: image with rectangles drawn and the bounding box info
    """
    imgObjects = img.copy()
    imgGray = cv2.cvtColor(imgObjects, cv2.COLOR_BGR2GRAY) # convert image to gray scale
    object = objectCascade.detectMultiScale(imgGray, scaleF, minN) # find face objects in image - detectMultiScale(image, scale factor, minimum neighbors)
    for (x, y, w, h) in object: # draw box around faces
        cv2.rectangle(imgObjects, (x, y), (x+w, y+h), (255, 0, 255), 6)
    return imgObjects, object


def main():
    img = cv2.imread("../Resources/group.JPG") # import image
    faceCascade = cv2.CascadeClassifier("../Resources/haarcascade_frontalface_default.xml") # import face detection classifier file
    imgObjects , objects = findObjects(img, faceCascade)
    cv2.imshow("Output", imgObjects)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()