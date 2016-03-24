import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sudoku.jpg')

rows, cols, ch = img.shape

pts1 = np.float32([[30,65], [368,52], [28,387], [389,390]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (300,300))

cv2.putText(img,'.',(30, 65), cv2.FONT_HERSHEY_COMPLEX, 10, (109,245,41))
cv2.putText(img,'.',(368, 52),cv2.FONT_HERSHEY_COMPLEX,10,(109,245,41))
cv2.putText(img,'.',(28, 387),cv2.FONT_HERSHEY_COMPLEX,10,(109,245,41))
cv2.putText(img,'.',(389, 390),cv2.FONT_HERSHEY_COMPLEX,10,(109,245,41))



plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show()

