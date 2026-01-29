import cv2

cam = cv2.VideoCapture(0)
#parameter is 0 for the inbuilt camera
#parameter 1 or 2 is for external cameras
#the external cameras number is defined by the usb ports number of the laptop
#video = 24frames per second

#ret = return
#cam.read() reads the camera

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video codec and output file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')   # you can also try 'MJPG' or 'mp4v'
out = cv2.VideoWriter("output.mp4v", fourcc, 20.0, (frame_width, frame_height))
while True:
    
    ret, frame = cam.read()
    cv2.putText(frame,"Dyothi Sai Lalitha",(50,50),5,2,(255,0,0))
    cv2.line(frame,(50,65), (510,65), (255,0,0),3)
    cv2.rectangle(frame,(510,20),(600,50), (255,0,0),2)
    cv2.circle(frame,(30,30), 20,(255,0,0),3)
    out.write(frame)
    cv2.imshow('Dyothi camera',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
out.release()
cv2.destroyAllWindows()
