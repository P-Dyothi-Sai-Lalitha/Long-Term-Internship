import cv2

cam = cv2.VideoCapture(0)
#parameter is 0 for the inbuilt camera
#parameter 1 or 2 is for external cameras
#the external cameras number is defined by the usb ports number of the laptop
#video = 24frames per second

#ret = return
#cam.read() reads the camera
while True:
    ret, frame = cam.read()

    cv2.imshow('camera',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows(camera)
