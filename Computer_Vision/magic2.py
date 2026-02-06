import cv2
import numpy as np
import time
cam = cv2.VideoCapture(0)
time.sleep(3)

for i in range(20):
    ret, background = cam.read()
while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red1,upper_red1)

    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red2,upper_red2)

    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.int8))
    cloak = cv2.bitwise_and(background,background,mask = mask)
    rest = cv2.bitwise_and(frame,frame, mask = cv2.bitwise_not(mask))
    final = cv2.add(cloak, rest)
    cv2.imshow('window', final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

