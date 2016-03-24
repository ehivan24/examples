import cv2
import numpy as np
img = cv2.imread('watch.JPG', cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,0,0),thickness=3)
cv2.rectangle(img,(15,25),(200,150),(0,45,255),thickness=5)
cv2.circle(img,(100,63),100,(255,0,255), thickness=-1)


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))

cv2.polylines(img,[pts],True,(0,255,255),thickness=1)


font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OPENCV2',(65,24),font,.8,(0,0,24 ), thickness=4)

cv2.imshow('watch', img)

cv2.waitKey(0)
cv2.destroyAllWindows()