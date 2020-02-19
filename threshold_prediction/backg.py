import cv2
import numpy as np
#creating an object which will read the frame from the webcam( indicated by the parameter zero)
cap = cv2.VideoCapture(r'C:\Users\HP\Pictures\Camera Roll\vid.mp4')
# creating an object of the class which uses Mixture of Gaussian for finding the foreground adaptively
backSub = cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame = cap.read()
# applying the mask to the given frame
    fgMask = backSub.apply(frame)
#displaying the original frame
    cv2.imshow('frame',frame)
#displaying the processed frame
    cv2.imshow('background',fgMask)
    c = cv2.waitKey(1)
    if(c==27):
        break
#clearing the buffer and destroying the object created
cap.release()
#destroying all windows
cv2.destroyAllWindows()
