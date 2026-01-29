import cv2

face_cascade = cv2.CascadeClassifier(r"data\haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

#scalefactor helps in reducing the % of image's different areas
#simply it cut downs the percentage of unnecessary parts
#minNeighbours help in confirming the difference in the colors with nighbouring pixels
#it works with a voting systems
#high value means high positive
#minSize determines the range of the searching

while True:
    ret, frame = cam.read()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors = 5,
                                     minSize = (30,30))

    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,255), 2)
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
