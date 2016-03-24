import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)


grayScale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayScale, 12, 255, cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(grayScale,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

retval3, otsu =cv2.threshold(grayScale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('image', img)
cv2.imshow('thres', threshold)
cv2.imshow('thres2', threshold2)
cv2.imshow('gauss', gauss)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()


