import cv2
import numpy as np

cap = cv2.VideoCapture('people-walking.mp4')


fgbg = cv2.BackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fb', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

#https://media.readthedocs.org/pdf/opencv-python-tutroals/latest/opencv-python-tutroals.pdf
#https://www.youtube.com/watch?v=6zPeIeUAhZM&index=3&list=PLGBJ5oXZOoGeGzg0W_uojaeMzpMgt39rT