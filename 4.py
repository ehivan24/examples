import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)




    cv2.imshow('frame2', frame2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




