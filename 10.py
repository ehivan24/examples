import cv2
import numpy as np

img = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

#merging two images, the image have to be the same size
px = img[50,50]

dst = cv2.addWeighted(img, 0.7, img2,0.3,0)

print img.shape
print img.size

ball = img[30:100, 23:150]
img[0:70, 0:127] =ball
cv2.imshow('watch', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
