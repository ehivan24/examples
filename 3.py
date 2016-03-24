import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("watch.JPG", cv2.IMREAD_GRAYSCALE)

#plt.plot(img)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([500, 100], [800, 400], 'c',linewidth=5 )
plt.show()
