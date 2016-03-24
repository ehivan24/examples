# Template Matching


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('opencv-template-matching-python-tutorial.jpg')
im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, 0)


template = cv2.imread('opencv-template-for-matching.jpg', 0)



w, h = template.shape[::-1]

res = cv2.matchTemplate(im_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()