#
# Tracking color via HSV Red and removing noise
# opening removes the positive ones and closing removes the negative ones
#

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])

    #dark_red = np.uint8([[12,22,121]])
    #dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    rest = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15,15), np.float32) / 225
    smoothed = cv2.filter2D(rest, -1, kernel)

    blur = cv2.GaussianBlur(rest, (15,15), 0)
    median = cv2.medianBlur(rest, 15)

    bilateral = cv2.bilateralFilter(rest, 15, 75, 75)

    kernel2 = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel2, iterations=1)
    dilatation = cv2.dilate(mask, kernel2, iterations=1)

    cv2.imshow('erosion', erosion)
    cv2.imshow('dialation', dilatation)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel2)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel2)

    #cv2.imshow('bilateral', bilateral)
    #cv2.imshow('mediam', median)
    #cv2.imshow('Blur', blur)
    #cv2.imshow('smothed', smoothed)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('rest', rest)
    #cv2.imshow('erosion', erosion)
    #cv2.imshow('dilatation', dilatation)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

