import cv2
import numpy as np
import time
cam = cv2.VideoCapture(0)
time.sleep(3)

for i in range(20):
    ret, background = cam.read()
while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([100,150,0])
    upper_red = np.array([140,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(background,background,mask = mask)
    body = cv2.bitwise_and(frame,frame, mask = cv2.bitwise_not(mask))
    final_result = cv2.add(result,body)
    cv2.imshow('window',final_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
